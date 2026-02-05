import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
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
OBJ_COLS = ["reviews", "sources"]


def to_df(schools):
    df = pd.DataFrame(schools).copy()

    # Ensure required columns exist
    for c in TEXT_COLS:
        if c not in df.columns:
            df[c] = ""
        df[c] = df[c].astype("string").fillna("")

    for c in NUM_COLS:
        if c not in df.columns:
            df[c] = pd.NA
        df[c] = pd.to_numeric(df[c], errors="coerce")

    for c in OBJ_COLS:
        if c not in df.columns:
            df[c] = pd.NA

    # Stable display label
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
        # list of dicts
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

    # single string fallback
    if isinstance(sources, str) and sources.strip():
        st.markdown(f"- {sources.strip()}")
    else:
        st.write("—")


def safe_float(x):
    try:
        return float(x)
    except Exception:
        return None


# -----------------------------
# Load & filters
# -----------------------------
df = to_df(SCHOOLS)

st.title("Valencia-area schools map (screen-light / low-device focus)")
st.caption("Click a pin to select a school. This version uses Leaflet (Folium) for reliable click events on Streamlit Cloud.")

with st.sidebar:
    st.header("Filters")

    # Type filter
    types = sorted([t for t in df["type"].unique().tolist() if t])
    type_sel = st.multiselect("School type", types, default=types)
    dff = df[df["type"].isin(type_sel)].copy()

    # Municipality filter
    munis = sorted([m for m in dff["municipality"].unique().tolist() if m])
    if munis:
        muni_sel = st.multiselect("Municipality", munis, default=munis)
        dff = dff[dff["municipality"].isin(muni_sel)].copy()

    # Search
    q = st.text_input("Search (name/address)", "")
    if q.strip():
        qq = q.strip().lower()
        dff = dff[
            dff["name"].str.lower().str.contains(qq, na=False)
            | dff["address"].str.lower().str.contains(qq, na=False)
        ].copy()

# Selection state
if "selected_id" not in st.session_state:
    st.session_state.selected_id = ""

if dff.empty:
    st.warning("No schools match the current filters.")
    st.stop()

if st.session_state.selected_id not in dff["id"].tolist():
    st.session_state.selected_id = dff.iloc[0]["id"]


# -----------------------------
# Missing coordinates warning
# -----------------------------
missing = dff[dff["lat"].isna() | dff["lon"].isna()][["name", "address"]]
if len(missing) > 0:
    st.sidebar.warning(f"{len(missing)} record(s) missing coordinates → they won’t appear as pins.")
    with st.sidebar.expander("Show missing"):
        for _, r in missing.iterrows():
            st.write(f"- {r['name']}: {r['address']}")


# -----------------------------
# Build map (Folium)
# -----------------------------
df_map = dff.dropna(subset=["lat", "lon"]).copy()

# Center map
if len(df_map) > 0:
    center_lat = float(df_map["lat"].mean())
    center_lon = float(df_map["lon"].mean())
    zoom = 11
else:
    center_lat, center_lon, zoom = 39.4699, -0.3763, 11

m = folium.Map(location=[center_lat, center_lon], zoom_start=zoom, control_scale=True)
cluster = MarkerCluster().add_to(m)

# Lookup for click-to-select: rounded coords -> school id
coord_to_id = {}

def add_marker(row, highlight=False):
    lat = safe_float(row["lat"])
    lon = safe_float(row["lon"])
    if lat is None or lon is None:
        return

    # rounding is important because click payload is floaty
    key = (round(lat, 6), round(lon, 6))
    coord_to_id[key] = row["id"]

    # color by type
    t = (row["type"] or "").lower()
    if "public" in t:
        color = "blue"
    elif "montessori" in (row["name"] or "").lower() or "waldorf" in (row["name"] or "").lower():
        color = "green"
    else:
        color = "purple"

    icon = folium.Icon(color=color, icon="info-sign")
    if highlight:
        # make the selected pin visually pop (slightly different icon color)
        icon = folium.Icon(color="red", icon="star")

    popup_html = f"""
    <div style="font-family: Arial; width: 320px;">
      <div style="font-size:14px; font-weight:700;">{row['name']}</div>
      <div style="font-size:12px; margin-top:4px;"><b>Type:</b> {row['type']}</div>
      <div style="font-size:12px; margin-top:4px;"><b>Address:</b> {row['address']}</div>
      <div style="font-size:12px; margin-top:6px;"><b>Device:</b> {row['device_policy_summary']}</div>
      <div style="font-size:12px; margin-top:6px; opacity:0.75;">Click pin → selects school</div>
    </div>
    """

    folium.Marker(
        location=[lat, lon],
        tooltip=row["name"],
        popup=folium.Popup(popup_html, max_width=450),
        icon=icon
    ).add_to(cluster)

# Add markers: draw others first, selected last (so it’s on top)
selected_id = st.session_state.selected_id
for _, r in df_map[df_map["id"] != selected_id].iterrows():
    add_marker(r, highlight=False)
for _, r in df_map[df_map["id"] == selected_id].iterrows():
    add_marker(r, highlight=True)


# -----------------------------
# Layout: map + list + portrait
# -----------------------------
left, right = st.columns([2, 1], gap="large")

with left:
    st.subheader("Map (click a pin)")
    map_state = st_folium(m, width=950, height=650)

    clicked = map_state.get("last_object_clicked")
    if clicked and "lat" in clicked and "lng" in clicked:
        ck = (round(float(clicked["lat"]), 6), round(float(clicked["lng"]), 6))
        new_id = coord_to_id.get(ck)
        if new_id and new_id != st.session_state.selected_id:
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
    )
    if chosen != st.session_state.selected_id:
        st.session_state.selected_id = chosen
        st.rerun()

with right:
    st.subheader("Selected school")
    row = df[df["id"] == st.session_state.selected_id]
    if row.empty:
        st.info("Select a school.")
    else:
        r = row.iloc[0]

        st.markdown(f"### {r['name']}")
        st.write(f"**Type:** {r['type']}")
        st.write(f"**Address:** {r['address']}")
        if r["municipality"]:
            st.write(f"**Municipality:** {r['municipality']}")

        if r["stages"]:
            st.write(f"**Stages:** {r['stages']}")
        if r["curriculum"]:
            st.write(f"**Curriculum:** {r['curriculum']}")
        if r["languages_day_to_day"]:
            st.write(f"**Languages (day-to-day):** {r['languages_day_to_day']}")
        if r["device_policy_summary"]:
            st.write(f"**Device policy (summary):** {r['device_policy_summary']}")
        if r["pedagogy"]:
            st.write(f"**Pedagogy:** {r['pedagogy']}")
        if r["coords_confidence"]:
            st.write(f"**Coordinate confidence:** {r['coords_confidence']}")

        if r["reviews"] is not None and r["reviews"] is not pd.NA and not (isinstance(r["reviews"], float) and pd.isna(r["reviews"])):
            st.markdown("**Reviews (snapshot):**")
            st.write(r["reviews"])

        if r["notes"]:
            st.caption(r["notes"])

        st.markdown("**Sources:**")
        render_sources(r["sources"])

st.divider()
st.caption("If clicking a pin doesn’t select, it’s almost always because two schools share the same rounded lat/lon. If that happens, tweak the rounding precision or make coords unique.")
