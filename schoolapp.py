# app.py
import re
import time
from typing import Dict, Any, List, Optional

import pandas as pd
import streamlit as st

# Mapping (Leaflet via Folium)
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# Geocoding (OpenStreetMap Nominatim)
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

st.set_page_config(page_title="Valencia School Map (Screen-light)", layout="wide")

# ----------------------------
# Data: your current shortlist
# ----------------------------
DEFAULT_SCHOOLS: List[Dict[str, Any]] = [
    {
        "rank": 1,
        "school": "Imagine Montessori School",
        "type": "Private",
        "address": "C/ Melissa 46, 46980 Paterna, Valencia, Spain",
        "why": "Montessori + English pathway through secondary; continuity through Primary+.",
        "device_policy": "No published grade-by-grade 1:1 device rollout found → request written confirmation.",
        "languages": "EN-led; ES support",
        "academic_proxy": "N/A (non-PAU pathway)",
        "sources": [
            ("Legal notice (address)", "https://imaginemontessori.es/aviso-legal/"),
        ],
    },
    {
        "rank": 2,
        "school": "Valencia Montessori School",
        "type": "Private",
        "address": "Av. Pío Baroja 3, 46015 València, Spain",
        "why": "AMI-style Montessori; strong early-years fit; likely screen-light culture.",
        "device_policy": "No public grade-by-grade 1:1 device rollout found → request written confirmation.",
        "languages": "EN primary; ES/VAL taught",
        "academic_proxy": "N/A (ends before PAU)",
        "sources": [
            ("Admissions / language model", "https://valenciamontessori.org/admissions/"),
            ("Listing with address", "https://www.international-schools-database.com/in/valencia-spain/valencia-montessori-school"),
        ],
    },
    {
        "rank": 3,
        "school": "Escuela Internacional Waldorf Valencia",
        "type": "Private / Association",
        "address": "Camino Cebolla 5, 46540 El Puig de Santa Maria, Valencia, Spain",
        "why": "Explicit ‘no screens in childhood’ stance; strong pedagogy fit through Primary.",
        "device_policy": "School states tech access begins from Secundaria (explicit on site).",
        "languages": "ES-led (+ EN; verify)",
        "academic_proxy": "N/A",
        "sources": [
            ("Why Waldorf (no screens + tech from Secundaria)", "https://escuelawaldorfvalencia.com/por-que-elegir-una-escuela-waldorf/"),
            ("Contact (address)", "https://escuelawaldorfvalencia.com/contacto/"),
        ],
    },
    {
        "rank": 4,
        "school": "British College La Cañada",
        "type": "Private",
        "address": "Calle 232 Nº110, 46182 La Cañada (Paterna), Valencia, Spain",
        "why": "Mainstream option with unusually clear, checkable tech policy.",
        "device_policy": "School states BYOD is implemented from KS4 to Sixth Form (published).",
        "languages": "EN-led + ES",
        "academic_proxy": "N/A (British exams)",
        "sources": [
            ("Digital learning policy", "https://www.britishcollegelacanyada.es/en/educational-project/digital-learning/"),
            ("Contact (address)", "https://www.britishcollegelacanyada.es/es/contacto/"),
        ],
    },
    {
        "rank": 5,
        "school": "Deutsche Schule Valencia / Colegio Alemán",
        "type": "Private",
        "address": "C/ Jaume Roig 14–16, 46010 València, Spain",
        "why": "Best Spanish–German pathway; academically strong.",
        "device_policy": "Tablets reported issued at 5º (via school post) → confirm full rollout in writing.",
        "languages": "DE + ES (+ EN)",
        "academic_proxy": "PAU not primary proxy",
        "sources": [
            ("Contact (address)", "https://dsvalencia.org/es/contacto/"),
            ("Tablet post (evidence)", "https://www.facebook.com/deutscheschulevalencia/posts/nuestros-nuevos-alumnos-de-5-curso-entran-en-la-era-digital-como-parte-de-nuestr/802012752121027/"),
        ],
    },
    {
        "rank": 6,
        "school": "Centro Educativo Gençana",
        "type": "Private / Concertado mix",
        "address": "C/ Ermita Nova 3, 46110 Godella, Valencia, Spain",
        "why": "Top academic reputation; trade-off on earlier 1:1 devices.",
        "device_policy": "Press profile reports Chromebook from 3º Primaria → verify latest in writing.",
        "languages": "ES/VAL + EN",
        "academic_proxy": "Reputation/demand proxy (replace PAU): high-demand + strong press profile",
        "sources": [
            ("El Mundo special PDF (device statement)", "https://fuenllana.net/wp-content/uploads/2024/03/240306-El-Mundo-Especial-colegios-Los-cien-ma%CC%81s-notables.pdf"),
            ("School site (address)", "https://www.gencana.es/"),
        ],
    },
    {
        "rank": 7,
        "school": "British School of Valencia (BSV)",
        "type": "Private",
        "address": "C/ Filipinas 37, 46006 València, Spain",
        "why": "In-city British option; strong pathway but weaker screen fit.",
        "device_policy": "School states 1:1 device programme from Year 3 to Year 13 (published).",
        "languages": "EN-led + ES",
        "academic_proxy": "N/A (British exams)",
        "sources": [
            ("Digital Learning Programme", "https://www.bsvalencia.com/digital-learning-programme/"),
            ("Campus page (address)", "https://www.bsvalencia.com/es/campus-bsv-nexus/"),
        ],
    },
    {
        "rank": 8,
        "school": "English School Los Olivos",
        "type": "Private",
        "address": "Campo Olivar, 46110 Godella, Valencia, Spain",
        "why": "English pathway with German offer; screen policy must be verified.",
        "device_policy": "No public grade-by-grade 1:1 rollout found → request written confirmation.",
        "languages": "EN-led + ES + DE",
        "academic_proxy": "N/A (British exams)",
        "sources": [
            ("Contact (addresses)", "https://www.los-olivos.es/contacto/"),
            ("Admissions/fees", "https://www.los-olivos.es/admisiones/"),
        ],
    },
    # Public CEIPs (top-rated list source)
    {
        "rank": 9,
        "school": "CEIP Municipal Benimaclet",
        "type": "Public",
        "address": "C/ de l'Arquitecte Arnau s/n, València, Spain",
        "why": "Top-rated public CEIP in Valencia city (directory proxy).",
        "device_policy": "Not published → ask school for written policy (1:1, homework platforms, take-home).",
        "languages": "ES / VAL",
        "academic_proxy": "MiCole top-rated public CEIP list",
        "sources": [
            ("MiCole public ranking list", "https://www.micole.net/valencia/mejores-colegios-publicos-de-valencia"),
        ],
    },
    {
        "rank": 10,
        "school": "CEIP Francisco Giner de los Ríos",
        "type": "Public",
        "address": "Plaça Grup Parpalló, València, Spain",
        "why": "Strong public reputation; good community fit (directory proxy).",
        "device_policy": "Not published → ask school for written policy.",
        "languages": "ES / VAL",
        "academic_proxy": "MiCole top-rated public CEIP list",
        "sources": [
            ("MiCole public ranking list", "https://www.micole.net/valencia/mejores-colegios-publicos-de-valencia"),
        ],
    },
    {
        "rank": 11,
        "school": "CEIP Rodríguez Fornos",
        "type": "Public",
        "address": "C/ de la Mare de Déu de la Cabeza 26, València, Spain",
        "why": "Consistently well-rated public option (directory proxy).",
        "device_policy": "Not published → ask school for written policy.",
        "languages": "ES / VAL",
        "academic_proxy": "MiCole top-rated public CEIP list",
        "sources": [
            ("MiCole public ranking list", "https://www.micole.net/valencia/mejores-colegios-publicos-de-valencia"),
        ],
    },
    {
        "rank": 12,
        "school": "CEIP Jaime Balmes",
        "type": "Public",
        "address": "C/ del Mestre Aguilar 15, València, Spain",
        "why": "High-demand public CEIP (directory proxy).",
        "device_policy": "Not published → ask school for written policy.",
        "languages": "ES / VAL",
        "academic_proxy": "MiCole top-rated public CEIP list",
        "sources": [
            ("MiCole public ranking list", "https://www.micole.net/valencia/mejores-colegios-publicos-de-valencia"),
        ],
    },
    {
        "rank": 13,
        "school": "CEIP IVAF–Luis Fortich",
        "type": "Public",
        "address": "C/ Juan de Garay 23, València, Spain",
        "why": "Strong inclusion + reputation (directory proxy).",
        "device_policy": "Not published → ask school for written policy.",
        "languages": "ES / VAL",
        "academic_proxy": "MiCole top-rated public CEIP list",
        "sources": [
            ("MiCole public ranking list", "https://www.micole.net/valencia/mejores-colegios-publicos-de-valencia"),
        ],
    },
]

# ---------------------------------
# Helpers
# ---------------------------------
def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())

@st.cache_data(show_spinner=False)
def schools_to_df(schools: List[Dict[str, Any]]) -> pd.DataFrame:
    rows = []
    for s in schools:
        src = " · ".join([f"{label}: {url}" for label, url in s.get("sources", [])])
        rows.append(
            {
                "rank": s.get("rank"),
                "school": s.get("school"),
                "type": s.get("type"),
                "address": s.get("address"),
                "why": s.get("why"),
                "device_policy": s.get("device_policy"),
                "languages": s.get("languages"),
                "academic_proxy": s.get("academic_proxy"),
                "sources": src,
                "lat": s.get("lat"),
                "lon": s.get("lon"),
            }
        )
    return pd.DataFrame(rows).sort_values("rank")

@st.cache_resource(show_spinner=False)
def get_geocoder():
    geolocator = Nominatim(user_agent="valencia-school-map")
    return RateLimiter(geolocator.geocode, min_delay_seconds=1, swallow_exceptions=True)

@st.cache_data(show_spinner=True)
def geocode_addresses(addresses: List[str]) -> Dict[str, Optional[Dict[str, float]]]:
    geocode = get_geocoder()
    out: Dict[str, Optional[Dict[str, float]]] = {}
    for a in addresses:
        if not a:
            out[a] = None
            continue
        loc = geocode(a)
        if loc:
            out[a] = {"lat": float(loc.latitude), "lon": float(loc.longitude)}
        else:
            out[a] = None
    return out

def make_popup_html(row: pd.Series) -> str:
    # Keep it compact (popup), full detail goes to sidebar.
    sources = row.get("sources", "")
    sources_html = ""
    if sources:
        items = []
        for part in sources.split(" · "):
            if ": " in part:
                label, url = part.split(": ", 1)
                items.append(f'<li><a href="{url}" target="_blank">{label}</a></li>')
        if items:
            sources_html = "<b>Sources</b><ul style='margin:0; padding-left:18px;'>" + "".join(items[:3]) + "</ul>"

    return f"""
    <div style="font-family: Arial; width: 320px;">
      <div style="font-size: 14px; font-weight: 700;">{row['rank']}. {row['school']}</div>
      <div style="font-size: 12px; margin-top: 4px;"><b>Type:</b> {row['type']}</div>
      <div style="font-size: 12px; margin-top: 4px;"><b>Address:</b> {row['address']}</div>
      <div style="font-size: 12px; margin-top: 6px;"><b>Device:</b> {row['device_policy']}</div>
      <div style="font-size: 12px; margin-top: 6px;"><b>Languages:</b> {row['languages']}</div>
      <div style="font-size: 12px; margin-top: 6px;"><b>Proxy:</b> {row['academic_proxy']}</div>
      <div style="font-size: 12px; margin-top: 6px;"><b>Why:</b> {row['why']}</div>
      {sources_html}
    </div>
    """

# ---------------------------------
# UI
# ---------------------------------
st.title("Valencia schools — screen-light shortlist map")
st.caption("Interactive map: click a pin to see a popup; select a school in the sidebar for the full portrait.")

# ---- session-state init ----
if "df" not in st.session_state:
    st.session_state.df = schools_to_df(DEFAULT_SCHOOLS)

df = st.session_state.df

with st.sidebar:
    st.header("Filters")
    types = sorted(df["type"].dropna().unique().tolist())
    selected_types = st.multiselect("School type", types, default=types)

    q = st.text_input("Search (name / address / language)", "")

    # Simple heuristics for device-policy filtering
    device_modes = [
        "All",
        "No 1:1 stated / needs confirmation",
        "Explicitly delayed / later (e.g., KS4 / Secundaria / 5º+)",
        "Early 1:1 reported (Year 3 / 3º Primaria etc.)",
    ]
    device_filter = st.selectbox("Device-policy lens", device_modes, index=0)

    st.divider()
    st.subheader("Geocoding")
    st.write("If pins don’t show (no lat/lon), click to geocode addresses via OpenStreetMap.")
    do_geocode = st.button("Geocode missing coordinates")

    st.divider()
    st.subheader("Select school (full portrait)")
    selected_school = st.selectbox("School", df["school"].tolist(), index=0)

# Apply filters
f = df[df["type"].isin(selected_types)].copy()

if q.strip():
    nq = normalize(q)
    mask = (
        f["school"].fillna("").map(normalize).str.contains(nq)
        | f["address"].fillna("").map(normalize).str.contains(nq)
        | f["languages"].fillna("").map(normalize).str.contains(nq)
    )
    f = f[mask]

if device_filter != "All":
    dp = f["device_policy"].fillna("").str.lower()
    if "needs confirmation" in device_filter.lower():
        f = f[dp.str.contains("confirm") | dp.str.contains("no public") | dp.str.contains("not published")]
    elif "delayed" in device_filter.lower():
        f = f[dp.str.contains("ks4") | dp.str.contains("secundaria") | dp.str.contains("5º") | dp.str.contains("later")]
    elif "early" in device_filter.lower():
        f = f[dp.str.contains("year 3") | dp.str.contains("3º") | dp.str.contains("chromebook from 3")]

# Geocode missing coords if requested
if do_geocode:
    missing_mask = df["lat"].isna() | df["lon"].isna()
    missing_addresses = df.loc[missing_mask, "address"].dropna().unique().tolist()

    if not missing_addresses:
        st.info("No missing coordinates in the current dataset.")
    else:
        res = geocode_addresses(missing_addresses)  # cached
        updated = 0
        for addr, coords in res.items():
            if coords:
                m = df["address"] == addr
                df.loc[m, "lat"] = coords["lat"]
                df.loc[m, "lon"] = coords["lon"]
                updated += int(m.sum())

        # Persist back to session state
        st.session_state.df = df

        st.success(f"Geocoding done. Updated {updated} rows.")
        st.rerun()


# Build map
# Default center: Valencia
center_lat, center_lon = 39.4699, -0.3763
m = folium.Map(location=[center_lat, center_lon], zoom_start=11, control_scale=True)

cluster = MarkerCluster().add_to(m)

# Use df (full) for coords availability, but show only filtered pins
display = df[df["school"].isin(f["school"])].copy()

for _, row in display.iterrows():
    lat, lon = row.get("lat"), row.get("lon")
    if pd.isna(lat) or pd.isna(lon):
        continue

    # Simple color logic
    dtype = str(row["type"]).lower()
    if "public" in dtype:
        color = "blue"
    elif "waldorf" in str(row["school"]).lower() or "montessori" in str(row["school"]).lower():
        color = "green"
    else:
        color = "purple"

    popup_html = make_popup_html(row)
    folium.Marker(
        location=[float(lat), float(lon)],
        popup=folium.Popup(popup_html, max_width=420),
        tooltip=f"{int(row['rank'])}. {row['school']}",
        icon=folium.Icon(color=color, icon="info-sign"),
    ).add_to(cluster)

col_map, col_detail = st.columns([1.35, 1])

with col_map:
    st.subheader("Map")
    st_folium(m, width=900, height=650)

with col_detail:
    st.subheader("Selected school — full portrait")
    r = df[df["school"] == selected_school].iloc[0]
    st.markdown(f"### {int(r['rank'])}. {r['school']}")
    st.write(f"**Type:** {r['type']}")
    st.write(f"**Address:** {r['address']}")
    st.write(f"**Languages:** {r['languages']}")
    st.write(f"**Device policy:** {r['device_policy']}")
    st.write(f"**Academic / reputation proxy:** {r['academic_proxy']}")
    st.write(f"**Why:** {r['why']}")

    # Sources as clickable links
    st.markdown("**Sources:**")
    sources_raw = r.get("sources", "")
    if sources_raw:
        for part in sources_raw.split(" · "):
            if ": " in part:
                label, url = part.split(": ", 1)
                st.markdown(f"- [{label}]({url})")
    else:
        st.write("—")

st.divider()
st.subheader("Data table (filtered)")
st.dataframe(f.drop(columns=["sources"], errors="ignore"), use_container_width=True)

st.caption(
    "Tip: If you want Google Maps tiles, you can swap the basemap with a Google tile layer, but you’ll need an API key. "
    "This app uses OpenStreetMap by default for stability and easier deployment."
)
