# app.py
import streamlit as st
import pandas as pd
import pydeck as pdk

from schools_data import SCHOOLS

st.set_page_config(page_title="Valencia Schools Map", layout="wide")

# ---- Load data ----
df = pd.DataFrame(SCHOOLS)

# Basic validation to prevent duplicates / missing coords
def validate(df: pd.DataFrame) -> list[str]:
    issues = []
    if df["name"].duplicated().any():
        dups = df[df["name"].duplicated()]["name"].tolist()
        issues.append(f"Duplicate school names: {sorted(set(dups))}")
    missing = df[df["lat"].isna() | df["lon"].isna()]
    if len(missing) > 0:
        issues.append(f"Missing coordinates for: {missing['name'].tolist()}")
    return issues

issues = validate(df)
if issues:
    st.error("Dataset issues detected:\n- " + "\n- ".join(issues))
    st.stop()

# ---- UI state ----
if "selected_school" not in st.session_state:
    st.session_state.selected_school = df.loc[0, "name"]

# ---- Sidebar filters ----
st.sidebar.header("Filters")
types = st.sidebar.multiselect("School type", sorted(df["type"].unique()), default=sorted(df["type"].unique()))
df_f = df[df["type"].isin(types)].copy()

query = st.sidebar.text_input("Search by name/address", "")
if query.strip():
    q = query.strip().lower()
    df_f = df_f[df_f.apply(lambda r: q in str(r["name"]).lower() or q in str(r["address"]).lower(), axis=1)]

st.title("Valencia early-years schools (screen-light focus)")

left, right = st.columns([0.42, 0.58], gap="large")

# ---- Left column: list + selected school card ----
with left:
    st.subheader("Schools")
    if df_f.empty:
        st.info("No schools match your filters.")
    else:
        # Use a radio so selection is immediate & stable
        selected = st.radio(
            label="Select a school",
            options=df_f["name"].tolist(),
            index=df_f["name"].tolist().index(st.session_state.selected_school) if st.session_state.selected_school in df_f["name"].tolist() else 0,
            label_visibility="collapsed",
        )
        st.session_state.selected_school = selected

    st.divider()
    st.subheader("Selected school")

    sel = df[df["name"] == st.session_state.selected_school].iloc[0]

    st.markdown(f"### {sel['name']}")
    st.write(f"**Type:** {sel['type']}")
    st.write(f"**Address:** {sel['address']}")
    st.write(f"**Ages:** {sel.get('ages','—')}")
    st.write(f"**Curriculum:** {sel.get('curriculum','—')}")
    st.write(f"**Languages:** {sel.get('languages','—')}")
    st.write(f"**Device / screen policy (to verify):** {sel.get('screen_policy','—')}")
    if sel.get("notes"):
        st.caption(sel["notes"])

    if sel.get("sources"):
        st.markdown("**Sources**")
        for url in sel["sources"]:
            st.markdown(f"- {url}")

# ---- Right column: map ----
with right:
    st.subheader("Map")

    # Center map on selected school
    view_state = pdk.ViewState(
        latitude=float(sel["lat"]),
        longitude=float(sel["lon"]),
        zoom=12,
        pitch=0,
    )

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df_f,
        get_position="[lon, lat]",
        get_radius=65,
        pickable=True,
    )

    tooltip = {
        "html": "<b>{name}</b><br/>{address}<br/><i>{type}</i>",
        "style": {"backgroundColor": "white", "color": "black"},
    }

    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip=tooltip,
        map_style=None,  # default
    )

    event = st.pydeck_chart(deck, use_container_width=True)

    # Optional: click-to-select based on tooltip pick (Streamlit/pydeck limitations vary by version)
    # For deterministic behavior, selection is driven by the radio list.

st.caption("No runtime geocoding: all coordinates are pre-filled in schools_data.py.")
