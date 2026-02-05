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


# -----------------------------
# Load data + filters
# -----------------------------
df = to_df(SCHOOLS)

st.title("Valencia-area schools map (screen-light / low-device focus)")
st.caption("Click a pin to select a school.")

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

# Initialize session state
if "selected_id" not in st.session_state:
    st.session_state.selected_id = ""
if "last_clicked" not in st.session_state:
    st.session_state.last_clicked = None
if "filter_hash" not in st.session_state:
    st.session_state.filter_hash = None

# Check if filters changed - if so, clear click tracking
current_filter_hash = hash(tuple(sorted(dff["id"].tolist())))
if st.session_state.filter_hash != current_filter_hash:
    st.session_state.filter_hash = current_filter_hash
    st.session_state.last_clicked = None

if st.session_state.selected_id not in dff["id"].tolist():
    st.session_state.selected_id = dff.iloc[0]["id"]


# Missing coords warning
missing = dff[dff["lat"].isna() | dff["lon"].isna()][["name", "address"]]
if len(missing) > 0:
    st.sidebar.warning(f"{len(missing)} record(s) missing coordinates → they won't appear as pins.")
    with st.sidebar.expander("Show missing"):
        for _, r in missing.iterrows():
            st.write(f"- {r['name']}: {r['address']}")


# -----------------------------
# Map with OpenStreetMap
# -----------------------------
df_map = dff.dropna(subset=["lat", "lon"]).copy()

# Center map on selected (if it has coords); else on mean; else Valencia center
selected_row = df[df["id"] == st.session_state.selected_id]
if not selected_row.empty and pd.notna(selected_row.iloc[0]["lat"]) and pd.notna(selected_row.iloc[0]["lon"]):
    center_lat = float(selected_row.iloc[0]["lat"])
    center_lon = float(selected_row.iloc[0]["lon"])
    zoom = 13
elif len(df_map) > 0:
    center_lat = float(df_map["lat"].mean())
    center_lon = float(df_map["lon"].mean())
    zoom = 11
else:
    center_lat, center_lon, zoom = 39.4699, -0.3763, 11

m = folium.Map(
    location=[center_lat, center_lon], 
    zoom_start=zoom, 
    control_scale=True,
    tiles='OpenStreetMap'
)

def marker_color(s_type: str, s_name: str) -> str:
    t = (s_type or "").lower()
    n = (s_name or "").lower()
    if "public" in t:
        return "blue"
    if "montessori" in n or "waldorf" in n:
        return "green"
    return "purple"

# Add markers with school IDs
for _, r in df_map.iterrows():
    lat, lon = float(r["lat"]), float(r["lon"])
    is_selected = (r["id"] == st.session_state.selected_id)
    
    if is_selected:
        color = "red"
        icon_name = "star"
        name_prefix = "⭐ "
    else:
        color = marker_color(r["type"], r["name"])
        icon_name = "info-sign"
        name_prefix = ""
    
    popup_html = f"""
    <div style="font-family: Arial; width: 340px;">
      <div style="font-size:14px; font-weight:700;">{name_prefix}{r['name']}</div>
      <div style="font-size:12px; margin-top:4px;"><b>Type:</b> {r['type']}</div>
      <div style="font-size:12px; margin-top:4px;"><b>Address:</b> {r['address']}</div>
      <div style="font-size:12px; margin-top:6px;"><b>Device:</b> {r['device_policy_summary']}</div>
    </div>
    """
    
    folium.Marker(
        location=[lat, lon],
        tooltip=r["name"],
        popup=folium.Popup(popup_html, max_width=480),
        icon=folium.Icon(color=color, icon=icon_name),
    ).add_to(m)


# -----------------------------
# Layout
# -----------------------------
left, right = st.columns([2, 1], gap="large")

with left:
    st.subheader("Map (click a pin to select)")
    
    # Use a stable key - dynamic keys cause issues
    map_state = st_folium(m, width=950, height=650, key="school_map")

    # Detect clicks - only process if coordinates actually changed
    if map_state and "last_object_clicked" in map_state:
        clicked = map_state["last_object_clicked"]
        if clicked and isinstance(clicked, dict) and len(df_map) > 0:
            click_lat = clicked.get("lat")
            click_lon = clicked.get("lng", clicked.get("lon"))
            
            if click_lat is not None and click_lon is not None:
                # Create a precise signature for this click
                click_signature = f"{float(click_lat):.7f},{float(click_lon):.7f}"
                
                # Only process if this is genuinely a NEW click
                if st.session_state.last_clicked != click_signature:
                    new_id = nearest_school_id(df_map, float(click_lat), float(click_lon), max_m=80)
                    
                    if new_id:
                        # Update tracking FIRST, before any state changes
                        st.session_state.last_clicked = click_signature
                        
                        # Only rerun if we're actually changing selection
                        if new_id != st.session_state.selected_id:
                            st.session_state.selected_id = new_id
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
        st.session_state.last_clicked = None  # Reset click tracking
        st.rerun()


# Helper function to check if value is empty (fixes TypeError)
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

        # Core sections
        def show(label, key):
            v = r.get(key)
            if is_empty(v):
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

        # Any extra fields beyond the known schema
        known = set(TEXT_COLS + NUM_COLS + ["label", "reviews", "sources"])
        extras = {k: v for k, v in r.items() if k not in known and not is_empty(v)}
        
        if extras:
            with st.expander("More details"):
                for k, v in extras.items():
                    st.write(f"**{k}:** {v}")

        # Reviews
        if not is_empty(r.get("reviews")):
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
