import math
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

from schools_data import SCHOOLS

st.set_page_config(page_title="Valencia school map (screen-light)", layout="wide")


# -----------------------------
# Robust schema handling
# -----------------------------
TEXT_COLS = [
    "id", "name", "type", "address", "municipality", "stages", "curriculum",
    "languages_day_to_day", "device_policy_summary", "pedagogy",
    "coords_confidence", "notes"
]
NUM_COLS = ["lat", "lon"]

def to_df(schools):
    df = pd.DataFrame(schools).copy()

    # Ensure minimal required fields
    if "id" not in df.columns:
        df["id"] = df.index.astype(str)
    if "name" not in df.columns:
        df["name"] = "Unnamed school"

    # Ensure text cols exist and are strings
    for c in TEXT_COLS:
        if c not in df.columns:
            df[c] = ""
        df[c] = df[c].astype("string").fillna("")

    # Ensure numeric cols exist and are numeric (NaN allowed)
    for c in NUM_COLS:
        if c not in df.columns:
            df[c] = pd.NA
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # Optional object fields
    if "sources" not in df.columns:
        df["sources"] = pd.NA
    if "reviews" not in df.columns:
        df["reviews"] = pd.NA

    # Display label
    df["label"] = df.apply(
        lambda r: f"{r['name']} — {r['type']}" + (f" ({r['municipality']})" if r["municipality"] else ""),
        axis=1
    )
    return df


def render_sources(sources):
    """sources expected: list[dict(label, ref)] but tolerate other shapes."""
    if sources is None or sources is pd.NA or (isinstance(sources, float) and pd.isna(sources)):
        st.write("—")
        return

    if isinstance(sources, list):
        if len(sources) == 0:
            st.write("—")
            return
        if isinstance(sources[0], dict):
            for s in sources:
                label = s.get("label", "Source")
                ref = s.get("ref", "")
                if ref:
                    st.markdown(f"- [{label}]({ref})")
        else:
            for ref in sources:
                if ref:
                    st.markdown(f"- {ref}")
        return

    if isinstance(sources, str) and sources.strip():
        st.markdown(f"- {sources.strip()}")
    else:
        st.write("—")


def _haversine_m(lat1, lon1, lat2, lon2):
    """Distance in meters."""
    R = 6371000.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dl/2)**2
    return 2 * R * math.asin(math.sqrt(a))


def nearest_school_id(df_map, click_lat, click_lon, max_m=50):
    """Map click lat/lon to the nearest school within max_m meters."""
    best_id = None
    best_d = None
    for _, r in df_map.iterrows():
        lat, lon = float(r["lat"]), float(r["lon"])
        d = _haversine_m(click_lat, click_lon, lat, lon)
        if best_d is None or d < best_d:
            best_d = d
            best_id = r["id"]
    if best_d is not None and best_d <= max_m:
        return best_id
    return None


def get_click_latlon(map_state: dict):
    """Try multiple keys streamlit-folium may emit depending on layer/click target."""
    if not isinstance(map_state, dict):
        return None

    candidates = [
        map_state.get("last_object_clicked"),
        map_state.get("last_object_clicked_popup"),
        map_state.get("last_object_clicked_tooltip"),
    ]
    for c in candidates:
        if isinstance(c, dict) and "lat" in c and ("lng" in c or "lon" in c):
            lat = c.get("lat")
            lon = c.get("lng", c.get("lon"))
            try:
                return float(lat), float(lon)
            except Exception:
                pass
    return None


# -----------------------------
# Load data + filters
# -----------------------------
df = to_df(SCHOOLS)

st.title("Valencia-area schools map (screen-light / low-device focus)")
st.caption("Click a pin to select a school. (No MarkerCluster — clicks are reliable on Streamlit Cloud.)")

with st.sidebar:
    st.header("Filters")

    types = sorted([t for t in df["type"].unique().tolist() if t])
    type_sel = st.multiselect("School type", types, default=types)
    dff = df[df["type"].isin(type_sel)].copy()

    munis = sorted([m for m in dff["municipality"].unique().tolist() if m])
    if munis:
        muni_sel = st.multiselect("Municipality", munis, default=munis)
        dff = dff[dff["municipality"].isin(muni_sel)].copy()

    q = st.text_input("Search (name/address)", "")
    if q.strip():
        qq = q.strip().lower()
        dff = dff[
            dff["name"].str.lower().str.contains(qq, na=False)
            | dff["address"].str.lower().str.contains(qq, na=False)
        ].copy()

if dff.empty:
    st.warning("No schools match the current filters.")
    st.stop()

if "selected_id" not in st.session_state:
    st.session_state.selected_id = ""

if st.session_state.selected_id not in dff["id"].tolist():
    st.session_state.selected_id = dff.iloc[0]["id"]


# Missing coords warning
missing = dff[dff["lat"].isna() | dff["lon"].isna()][["name", "address"]]
if len(missing) > 0:
    st.sidebar.warning(f"{len(missing)} record(s) missing coordinates → they won’t appear as pins.")
    with st.sidebar.expander("Show missing"):
        for _, r in missing.iterrows():
            st.write(f"- {r['name']}: {r['address']}")


# -----------------------------
# Map (NO MarkerCluster)
# -----------------------------
df_map = dff.dropna(subset=["lat", "lon"]).copy()

# Center map on selected (if it has coords); else on mean; else Valencia center
selected_row = df[df["id"] == st.session_state.selected_id]
if not selected_row.empty and pd.notna(selected_row.iloc[0]["lat"]) and pd.notna(selected_row.iloc[0]["lon"]):
    center_lat = float(selected_row.iloc[0]["lat"])
    center_lon = float(selected_row.iloc[0]["lon"])
    zoom = 12
elif len(df_map) > 0:
    center_lat = float(df_map["lat"].mean())
    center_lon = float(df_map["lon"].mean())
    zoom = 11
else:
    center_lat, center_lon, zoom = 39.4699, -0.3763, 11

m = folium.Map(location=[center_lat, center_lon], zoom_start=zoom, control_scale=True)

def marker_color(s_type: str, s_name: str) -> str:
    t = (s_type or "").lower()
    n = (s_name or "").lower()
    if "public" in t:
        return "blue"
    if "montessori" in n or "waldorf" in n:
        return "green"
    return "purple"

# Add markers (selected last + different icon)
for _, r in df_map[df_map["id"] != st.session_state.selected_id].iterrows():
    lat, lon = float(r["lat"]), float(r["lon"])
    color = marker_color(r["type"], r["name"])
    popup_html = f"""
    <div style="font-family: Arial; width: 340px;">
      <div style="font-size:14px; font-weight:700;">{r['name']}</div>
      <div style="font-size:12px; margin-top:4px;"><b>Type:</b> {r['type']}</div>
      <div style="font-size:12px; margin-top:4px;"><b>Address:</b> {r['address']}</div>
      <div style="font-size:12px; margin-top:6px;"><b>Device:</b> {r['device_policy_summary']}</div>
      <div style="font-size:12px; margin-top:6px; opacity:0.75;">Click pin → selects school</div>
    </div>
    """
    folium.Marker(
        location=[lat, lon],
        tooltip=r["name"],
        popup=folium.Popup(popup_html, max_width=480),
        icon=folium.Icon(color=color, icon="info-sign"),
    ).add_to(m)

# Selected marker on top
sel_map = df_map[df_map["id"] == st.session_state.selected_id]
for _, r in sel_map.iterrows():
    lat, lon = float(r["lat"]), float(r["lon"])
    popup_html = f"""
    <div style="font-family: Arial; width: 340px;">
      <div style="font-size:14px; font-weight:700;">⭐ {r['name']}</div>
      <div style="font-size:12px; margin-top:4px;"><b>Type:</b> {r['type']}</div>
      <div style="font-size:12px; margin-top:4px;"><b>Address:</b> {r['address']}</div>
    </div>
    """
    folium.Marker(
        location=[lat, lon],
        tooltip=f"Selected: {r['name']}",
        popup=folium.Popup(popup_html, max_width=480),
        icon=folium.Icon(color="red", icon="star"),
    ).add_to(m)


# -----------------------------
# Layout
# -----------------------------
left, right = st.columns([2, 1], gap="large")

with left:
    st.subheader("Map (click a pin to select)")
    map_state = st_folium(m, width=950, height=650, key="school_map")

    click = get_click_latlon(map_state)
    if click and len(df_map) > 0:
        click_lat, click_lon = click
        new_id = nearest_school_id(df_map, click_lat, click_lon, max_m=80)
        if new_id and new_id != st.session_state.selected_id:
            st.session_state.selected_id = new_id
            # Clear the map state to prevent re-triggering
            if 'last_rerun_id' not in st.session_state:
                st.session_state.last_rerun_id = None
            if st.session_state.last_rerun_id != new_id:
                st.session_state.last_rerun_id = new_id
                st.rerun()

    st.subheader("School list (manual select)")
    options = dff["id"].tolist()
    labels = dict(zip(dff["id"], dff["label"]))
    idx = options.index(st.session_state.selected_id) if st.session_state.selected_id in options else 0
    chosen = st.radio(
        label="",
        options=options,
        index=idx,
        format_func=lambda oid: labels.get(oid, oid),
        label_visibility="collapsed",
        key="school_list_radio",
    )
    if chosen != st.session_state.selected_id:
        st.session_state.selected_id = chosen
        st.rerun()


with right:
    st.subheader("Selected school — full portrait")
    row = df[df["id"] == st.session_state.selected_id]
    if row.empty:
        st.info("Select a school.")
    else:
        r = row.iloc[0].to_dict()

        # Header
        st.markdown(f"### {r.get('name','')}")
        st.write(f"**Type:** {r.get('type','')}")
        st.write(f"**Address:** {r.get('address','')}")
        if r.get("municipality"):
            st.write(f"**Municipality:** {r.get('municipality','')}")

        # Core sections (keeps your richer info once you upload the full dataset)
        def show(label, key):
            v = r.get(key)
            if v is None:
                return
            if isinstance(v, float) and pd.isna(v):
                return
            if v is pd.NA:
                return
            s = str(v).strip()
            if not s:
                return
            st.write(f"**{label}:** {s}")

        show("Stages", "stages")
        show("Curriculum", "curriculum")
        show("Languages (day-to-day)", "languages_day_to_day")
        show("Device policy (summary)", "device_policy_summary")
        show("Pedagogy", "pedagogy")
        show("Coordinate confidence", "coords_confidence")

        # Any extra fields beyond the known schema (future-proof for PDF-derived enrichments)
        known = set(TEXT_COLS + NUM_COLS + ["label", "reviews", "sources"])
        extras = {k: v for k, v in r.items() if k not in known}
        def is_empty(v):
            if v is None or v is pd.NA:
                return True
            if isinstance(v, str) and not v.strip():
                return True
            if isinstance(v, float):
                try:
                    return pd.isna(v)
                except:
                    return False
            return False
        
        extras = {k: v for k, v in extras.items() if not is_empty(v)}

        
        if extras:
            with st.expander("More details"):
                for k, v in extras.items():
                    st.write(f"**{k}:** {v}")

        # Reviews
        if r.get("reviews") not in (None, "", pd.NA) and not (isinstance(r.get("reviews"), float) and pd.isna(r.get("reviews"))):
            with st.expander("Reviews snapshot"):
                st.write(r["reviews"])

        # Notes
        if str(r.get("notes", "")).strip():
            st.caption(r["notes"])

        # Sources
        st.markdown("**Sources:**")
        render_sources(r.get("sources"))

st.divider()
st.caption("Pin-click selection works by mapping your click to the nearest school within ~80m. If two schools share nearly identical coords, increase precision in schools_data.py.")
