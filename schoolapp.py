import streamlit as st
import pandas as pd
import pydeck as pdk

from schools_data import SCHOOLS

st.set_page_config(page_title="Valencia school map (screen-light)", layout="wide")

# ---- helpers ----
def to_df(schools):
    df = pd.DataFrame(schools).copy()

    # --- enforce schema (CRITICAL) ---
    REQUIRED_COLUMNS = {
        "municipality": "",
        "lat": None,
        "lon": None,
        "type": "Unknown",
    }

    for col, default in REQUIRED_COLUMNS.items():
        if col not in df.columns:
            df[col] = default
        else:
            df[col] = df[col].fillna(default)

    # numeric safety
    df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
    df["lon"] = pd.to_numeric(df["lon"], errors="coerce")

    return df
def render_sources(src_list):
    if not src_list:
        return
    for s in src_list:
        label = s.get("label","Source")
        ref = s.get("ref","")
        if ref:
            st.markdown(f"- [{label}]({ref})")

# ---- data ----
df = to_df(SCHOOLS)

st.title("Valencia-area schools map (screen-light / low-device focus)")
st.caption("Pins rely on pre-filled coordinates (no runtime geocoding). Schools without coordinates will not appear on the map.")

# ---- sidebar filters ----
st.sidebar.header("Filters")
types = sorted(df["type"].dropna().unique().tolist())
type_sel = st.sidebar.multiselect("School type", types, default=types)

munis = sorted([m for m in df["municipality"].dropna().unique().tolist() if m])
muni_sel = st.sidebar.multiselect("Municipality", munis, default=munis)

query = st.sidebar.text_input("Search (name / address)", "")

df_f = df[df["type"].isin(type_sel)].copy()
df_f = df_f[df_f["municipality"].isin(muni_sel)].copy()
if query.strip():
    q = query.strip().lower()
    df_f = df_f[df_f.apply(lambda r: q in str(r.get("name","")).lower() or q in str(r.get("address","")).lower(), axis=1)].copy()

# ---- selection state ----
if "selected_id" not in st.session_state:
    st.session_state.selected_id = None

# select first visible if none selected
if st.session_state.selected_id is None and len(df_f) > 0:
    st.session_state.selected_id = df_f.iloc[0]["id"]

# ---- layout ----
left, right = st.columns([2, 1], gap="large")

with left:
    st.subheader("Map")

    df_map = df_f.dropna(subset=["lat","lon"]).copy()

    # center map
    if len(df_map) > 0:
        center_lat = float(df_map["lat"].mean())
        center_lon = float(df_map["lon"].mean())
        zoom = 10.5
    else:
        center_lat, center_lon, zoom = 39.4699, -0.3763, 10.0  # Valencia center fallback

    # separate selected pin
    selected = df_map[df_map["id"] == st.session_state.selected_id]
    others = df_map[df_map["id"] != st.session_state.selected_id]

    layers = []
    if len(others) > 0:
        layers.append(
            pdk.Layer(
                "ScatterplotLayer",
                data=others,
                get_position='[lon, lat]',
                get_radius=110,
                pickable=True,
                auto_highlight=True,
                tooltip=True,
            )
        )
    if len(selected) > 0:
        layers.append(
            pdk.Layer(
                "ScatterplotLayer",
                data=selected,
                get_position='[lon, lat]',
                get_radius=180,
                pickable=True,
                auto_highlight=True,
            )
        )

    # NOTE: pydeck tooltip uses fields from data
    view_state = pdk.ViewState(latitude=center_lat, longitude=center_lon, zoom=zoom)

    deck = pdk.Deck(
        map_style="mapbox://styles/mapbox/streets-v11",
        initial_view_state=view_state,
        layers=layers,
        tooltip={"text": "{name}\n{type}\n{address}"},
    )

    st.pydeck_chart(deck, use_container_width=True)

    st.subheader("School list (click to select)")
    # clickable list via radio
    options = df_f["id"].tolist()
    labels = df_f.apply(lambda r: f"{r['name']} — {r['type']} ({r['municipality']})", axis=1).tolist()
    idx = options.index(st.session_state.selected_id) if st.session_state.selected_id in options else 0

    chosen = st.radio("",
                      options=options,
                      index=idx,
                      format_func=lambda oid: labels[options.index(oid)],
                      label_visibility="collapsed")
    st.session_state.selected_id = chosen

with right:
    st.subheader("Selected school")
    row = df[df["id"] == st.session_state.selected_id]
    if len(row) == 0:
        st.info("Select a school from the list.")
    else:
        r = row.iloc[0].to_dict()
        st.markdown(f"### {r.get('name','')}")
        st.markdown(f"**Type:** {r.get('type','')}")
        st.markdown(f"**Address:** {r.get('address','')}")
        st.markdown(f"**Stages:** {r.get('stages','')}")
        st.markdown(f"**Curriculum:** {r.get('curriculum','')}")
        st.markdown(f"**Languages:** {r.get('languages_day_to_day','')}")
        st.markdown(f"**Device policy (summary):** {r.get('device_policy_summary','')}")
        st.markdown(f"**Pedagogy:** {r.get('pedagogy','')}")
        st.markdown(f"**Coordinate confidence:** {r.get('coords_confidence','')}")

        reviews = r.get("reviews") or {}
        if any(v is not None for v in reviews.values()):
            st.markdown("**Reviews (snapshot):**")
            st.write(reviews)

        if r.get("notes"):
            st.markdown(f"**Notes:** {r['notes']}")

        st.markdown("**Sources:**")
        render_sources(r.get("sources") or [])

st.divider()
st.caption("Tip: If any pin looks off, search the address in Google Maps once and update lat/lon in schools_data.py.")

