# app.py
import re
from typing import Dict, Any, List, Optional, Tuple

import pandas as pd
import streamlit as st

import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

from schools_data import SCHOOLS


# -------------------------
# Page config
# -------------------------
st.set_page_config(page_title="Valencia School Map (Screen-light)", layout="wide")


# -------------------------
# Helpers
# -------------------------
def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())

@st.cache_resource(show_spinner=False)
def get_geocoder():
    geolocator = Nominatim(user_agent="valencia-school-map")
    return RateLimiter(geolocator.geocode, min_delay_seconds=1, swallow_exceptions=True)

@st.cache_data(show_spinner=True)
def geocode_addresses(addresses: List[str]) -> Dict[str, Optional[Dict[str, float]]]:
    geocode = get_geocoder()
    out: Dict[str, Optional[Dict[str, float]]] = {}
    for a in addresses:
        loc = geocode(a)
        if loc:
            out[a] = {"lat": float(loc.latitude), "lon": float(loc.longitude)}
        else:
            out[a] = None
    return out

def schools_to_df(schools: List[Dict[str, Any]]) -> pd.DataFrame:
    rows = []
    for s in schools:
        rows.append({
            "rank": s.get("rank"),
            "school": s.get("school"),
            "type": s.get("type"),
            "address": s.get("address"),
            "why": s.get("why"),
            "device_policy": s.get("device_policy"),
            "languages": s.get("languages"),
            "academic_proxy": s.get("academic_proxy"),
            "sources": s.get("sources", []),
            "lat": s.get("lat"),
            "lon": s.get("lon"),
        })
    return pd.DataFrame(rows).sort_values("rank").reset_index(drop=True)

def device_bucket(device_policy: str) -> str:
    dp = (device_policy or "").lower()
    if any(k in dp for k in ["year 3", "3º", "chromebook from 3", "1:1 programme from year 3"]):
        return "Early 1:1 reported"
    if any(k in dp for k in ["ks4", "secundaria", "5º"]):
        return "Explicitly delayed"
    if any(k in dp for k in ["confirm", "not published", "no public"]):
        return "Needs written confirmation"
    return "Unclear"

def popup_html(row: pd.Series) -> str:
    src_items = []
    for label, url in row["sources"][:3]:
        src_items.append(f'<li><a href="{url}" target="_blank">{label}</a></li>')
    sources_html = ""
    if src_items:
        sources_html = "<b>Sources</b><ul style='margin:0; padding-left:18px;'>" + "".join(src_items) + "</ul>"

    return f"""
    <div style="font-family: Arial; width: 310px;">
      <div style="font-size: 14px; font-weight: 700;">{int(row['rank'])}. {row['school']}</div>
      <div style="font-size: 12px; margin-top: 4px;"><b>Type:</b> {row['type']}</div>
      <div style="font-size: 12px; margin-top: 4px;"><b>Languages:</b> {row['languages']}</div>
      <div style="font-size: 12px; margin-top: 6px;"><b>Device:</b> {row['device_policy']}</div>
      {sources_html}
      <div style="font-size: 11px; margin-top: 6px; opacity:0.8;">Click pin → portrait updates</div>
    </div>
    """


# -------------------------
# Session state init
# -------------------------
if "df" not in st.session_state:
    st.session_state.df = schools_to_df(SCHOOLS)

if "selected_school" not in st.session_state:
    st.session_state.selected_school = None

df = st.session_state.df


# -------------------------
# Header
# -------------------------
st.title("Valencia schools — screen-light shortlist (interactive map)")
st.caption("Click a pin to update the portrait. Use filters and geocode missing coordinates if needed.")


# -------------------------
# Sidebar controls
# -------------------------
with st.sidebar:
    st.header("Filters")

    types = sorted(df["type"].dropna().unique().tolist())
    selected_types = st.multiselect("School type", types, default=types)

    search = st.text_input("Search (name/address/languages)", "")

    device_modes = ["All", "Needs written confirmation", "Explicitly delayed", "Early 1:1 reported"]
    device_filter = st.selectbox("Device-policy bucket", device_modes, index=0)

    st.divider()
    st.subheader("Geocoding")
    st.write("Geocode missing coordinates via OpenStreetMap (cached).")
    do_geocode = st.button("Geocode missing coordinates")

    st.divider()
    st.subheader("Select school (manual)")
    # Keep selectbox in sync with clicks
    school_list = df["school"].tolist()
    default_idx = 0
    if st.session_state.selected_school in school_list:
        default_idx = school_list.index(st.session_state.selected_school)

    chosen = st.selectbox("School", school_list, index=default_idx)
    if chosen != st.session_state.selected_school:
        st.session_state.selected_school = chosen


# -------------------------
# Apply filters
# -------------------------
f = df[df["type"].isin(selected_types)].copy()

if search.strip():
    q = normalize(search)
    mask = (
        f["school"].fillna("").map(normalize).str.contains(q)
        | f["address"].fillna("").map(normalize).str.contains(q)
        | f["languages"].fillna("").map(normalize).str.contains(q)
    )
    f = f[mask]

if device_filter != "All":
    f = f[f["device_policy"].apply(device_bucket) == device_filter]


# -------------------------
# Geocoding (persist results)
# -------------------------
if do_geocode:
    # Only geocode rows with missing lat/lon and a "geocodable" address
    missing = df[(df["lat"].isna()) | (df["lon"].isna())].copy()

    # Avoid geocoding the Valencia Montessori entry while it has two addresses in one field
    # (You can fix it later by setting a single confirmed address.)
    def is_geocodable(addr: str) -> bool:
        if not addr:
            return False
        return "Published addresses vary:" not in addr

    missing = missing[missing["address"].apply(is_geocodable)]
    addresses = missing["address"].dropna().unique().tolist()

    if not addresses:
        st.info("No geocodable missing coordinates found (some addresses need manual confirmation).")
    else:
        res = geocode_addresses(addresses)
        updates = 0
        for addr, coords in res.items():
            if coords:
                m = df["address"] == addr
                df.loc[m, "lat"] = coords["lat"]
                df.loc[m, "lon"] = coords["lon"]
                updates += int(m.sum())

        st.session_state.df = df
        st.success(f"Geocoding complete. Updated {updates} rows.")
        st.rerun()


# -------------------------
# Build map
# -------------------------
center_lat, center_lon = 39.4699, -0.3763
m = folium.Map(location=[center_lat, center_lon], zoom_start=11, control_scale=True)

cluster = MarkerCluster().add_to(m)

# Build lookup from coordinate -> school for click mapping
coord_to_school: Dict[Tuple[float, float], str] = {}

# Only show pins for filtered set
display = df[df["school"].isin(f["school"])].copy()

for _, row in display.iterrows():
    lat, lon = row.get("lat"), row.get("lon")
    if pd.isna(lat) or pd.isna(lon):
        continue

    # Color logic
    dtype = str(row["type"]).lower()
    if "public" in dtype:
        color = "blue"
    elif "waldorf" in str(row["school"]).lower() or "montessori" in str(row["school"]).lower():
        color = "green"
    else:
        color = "purple"

    key = (round(float(lat), 6), round(float(lon), 6))
    coord_to_school[key] = row["school"]

    folium.Marker(
        location=[float(lat), float(lon)],
        popup=folium.Popup(popup_html(row), max_width=420),
        tooltip=f"{int(row['rank'])}. {row['school']}",
        icon=folium.Icon(color=color, icon="info-sign"),
    ).add_to(cluster)

st.session_state.coord_to_school = coord_to_school


# -------------------------
# Layout: map + portrait
# -------------------------
col_map, col_detail = st.columns([1.35, 1])

with col_map:
    st.subheader("Map")
    map_state = st_folium(m, width=900, height=650)

    clicked = map_state.get("last_object_clicked")
    if clicked and "lat" in clicked and "lng" in clicked:
        key = (round(float(clicked["lat"]), 6), round(float(clicked["lng"]), 6))
        school = st.session_state.coord_to_school.get(key)
        if school and st.session_state.selected_school != school:
            st.session_state.selected_school = school
            st.rerun()

with col_detail:
    st.subheader("Selected school — full portrait")

    selected = st.session_state.selected_school or df["school"].iloc[0]
    r = df[df["school"] == selected].iloc[0]

    st.markdown(f"### {int(r['rank'])}. {r['school']}")
    st.write(f"**Type:** {r['type']}")
    st.write(f"**Address:** {r['address']}")
    st.write(f"**Languages:** {r['languages']}")
    st.write(f"**Device policy:** {r['device_policy']}")
    st.write(f"**Academic / reputation proxy:** {r['academic_proxy']}")
    st.write(f"**Why:** {r['why']}")

    st.markdown("**Sources:**")
    if r["sources"]:
        for label, url in r["sources"]:
            st.markdown(f"- [{label}]({url})")
    else:
        st.write("—")


# -------------------------
# Data table
# -------------------------
st.divider()
st.subheader("Data (filtered)")
df_view = f.copy()
df_view["device_bucket"] = df_view["device_policy"].apply(device_bucket)
df_view = df_view.drop(columns=["sources"], errors="ignore")
st.dataframe(df_view, use_container_width=True)

st.caption(
    "Pins require coordinates. Use 'Geocode missing coordinates' or set lat/lon manually in schools_data.py "
    "for maximum stability."
)
