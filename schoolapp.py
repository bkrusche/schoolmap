import streamlit as st
import folium
from streamlit_folium import st_folium
from schools_data import SCHOOLS

# Page config
st.set_page_config(
    page_title="Valencia Schools Explorer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for cleaner look
st.markdown("""
    <style>
    .main > div {
        padding-top: 2rem;
    }
    h1 {
        color: #1f77b4;
        font-weight: 600;
    }
    .school-header {
        color: #2c3e50;
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .school-type {
        color: #7f8c8d;
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }
    .info-label {
        color: #34495e;
        font-weight: 600;
        margin-top: 0.8rem;
    }
    .info-value {
        color: #555;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "selected_school" not in st.session_state:
    st.session_state.selected_school = None

# Create the map
def create_map():
    # Calculate center of all schools
    lats = [s["lat"] for s in SCHOOLS]
    lons = [s["lon"] for s in SCHOOLS]
    center_lat = sum(lats) / len(lats)
    center_lon = sum(lons) / len(lons)
    
    # Create map with OpenStreetMap tiles
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=11,
        tiles="OpenStreetMap",
        control_scale=True
    )
    
    # Add markers for each school
    for idx, school in enumerate(SCHOOLS):
        # Color code: blue for public, red for private
        color = "blue" if school["type"].lower() == "public" else "lightred"
        icon = "graduation-cap"
        
        # Create popup content
        popup_html = f"""
        <div style="font-family: Arial; min-width: 200px; max-width: 300px;">
            <b style="font-size: 14px; color: #2c3e50;">{school['name']}</b><br>
            <span style="font-size: 12px; color: #7f8c8d;">{school['type']} School</span><br>
            <span style="font-size: 11px; color: #95a5a6; margin-top: 4px; display: block;">
                Click for details
            </span>
        </div>
        """
        
        folium.Marker(
            location=[school["lat"], school["lon"]],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=school["name"],
            icon=folium.Icon(color=color, icon=icon, prefix='fa')
        ).add_to(m)
    
    return m

# Main layout
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.title("🎓 Valencia Schools Explorer")
    st.markdown("**Click any pin on the map to see school details**")
    st.caption("🔵 Public Schools  |  🔴 Private Schools")
    
    # Render map
    m = create_map()
    map_data = st_folium(
        m,
        width=None,
        height=600,
        returned_objects=["last_object_clicked"]
    )
    
    # Detect which school was clicked
    if map_data and map_data.get("last_object_clicked"):
        clicked_lat = map_data["last_object_clicked"].get("lat")
        clicked_lng = map_data["last_object_clicked"].get("lng")
        
        if clicked_lat and clicked_lng:
            # Find the school at these coordinates (with small tolerance)
            for school in SCHOOLS:
                if abs(school["lat"] - clicked_lat) < 0.001 and abs(school["lon"] - clicked_lng) < 0.001:
                    st.session_state.selected_school = school
                    break

with col2:
    st.markdown("### 📋 School Information")
    
    if st.session_state.selected_school:
        school = st.session_state.selected_school
        
        # School header
        st.markdown(f'<div class="school-header">{school["name"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="school-type">{school["type"]} School</div>', unsafe_allow_html=True)
        
        # Address
        st.markdown('<div class="info-label">📍 Address</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="info-value">{school["address"]}</div>', unsafe_allow_html=True)
        
        # Ages
        if "ages" in school and school["ages"]:
            st.markdown('<div class="info-label">👶 Ages</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["ages"]}</div>', unsafe_allow_html=True)
        
        # Curriculum
        if "curriculum" in school and school["curriculum"]:
            st.markdown('<div class="info-label">📚 Curriculum</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["curriculum"]}</div>', unsafe_allow_html=True)
        
        # Languages
        if "languages" in school and school["languages"]:
            st.markdown('<div class="info-label">🌐 Languages</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["languages"]}</div>', unsafe_allow_html=True)
        
        # Screen Policy
        if "screen_policy" in school and school["screen_policy"]:
            st.markdown('<div class="info-label">💻 Screen Policy</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["screen_policy"]}</div>', unsafe_allow_html=True)
        
        # Notes
        if "notes" in school and school["notes"]:
            st.markdown('<div class="info-label">📝 Notes</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["notes"]}</div>', unsafe_allow_html=True)
        
        # Sources
        if "sources" in school and school["sources"]:
            st.markdown('<div class="info-label">🔗 Sources</div>', unsafe_allow_html=True)
            for source in school["sources"]:
                st.markdown(f"- [{source}]({source})", unsafe_allow_html=True)
        
        st.divider()
        
        # Google Maps link
        gmaps_url = f"https://www.google.com/maps/search/?api=1&query={school['lat']},{school['lon']}"
        st.markdown(f"[🗺️ Open in Google Maps]({gmaps_url})")
        
    else:
        st.info("👆 Click a school pin on the map to view details")
        
        # Show school count
        st.divider()
        st.metric("Total Schools", len(SCHOOLS))
        
        public_count = sum(1 for s in SCHOOLS if s["type"].lower() == "public")
        private_count = len(SCHOOLS) - public_count
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Public", public_count)
        with col_b:
            st.metric("Private", private_count)
