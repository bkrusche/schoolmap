import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

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

# Load schools data from CSV
@st.cache_data
def load_schools():
    """Load schools from CSV file and convert to list of dictionaries"""
    # Read CSV and drop any completely empty columns
    df = pd.read_csv('school_data.csv')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]  # Remove unnamed columns
    
    # Convert NaN to None for cleaner handling
    df = df.where(pd.notnull(df), None)
    
    # Convert to records
    schools = df.to_dict('records')
    
    # Clean up any remaining issues
    for school in schools:
        # Ensure numeric fields are properly typed
        if school.get('lat'):
            try:
                school['lat'] = float(school['lat'])
            except (ValueError, TypeError):
                school['lat'] = None
        if school.get('lon'):
            try:
                school['lon'] = float(school['lon'])
            except (ValueError, TypeError):
                school['lon'] = None
        if school.get('founded'):
            try:
                school['founded'] = int(school['founded'])
            except (ValueError, TypeError):
                school['founded'] = None
    
    return schools

SCHOOLS = load_schools()

# Initialize session state
if "selected_school" not in st.session_state:
    st.session_state.selected_school = None

# Create the map
def create_map():
    # Calculate center of all schools with valid coordinates
    valid_schools = [s for s in SCHOOLS if s.get('lat') and s.get('lon')]
    
    if not valid_schools:
        # Default to Valencia center if no valid coordinates
        center_lat, center_lon = 39.4699, -0.3763
    else:
        lats = [float(s["lat"]) for s in valid_schools]
        lons = [float(s["lon"]) for s in valid_schools]
        center_lat = sum(lats) / len(lats)
        center_lon = sum(lons) / len(lons)
    
    # Create map with minimal black and white style
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=11,
        tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        control_scale=True
    )
    
    # Add markers for each school with valid coordinates
    for idx, school in enumerate(SCHOOLS):
        # Skip schools without valid coordinates
        if not school.get('lat') or not school.get('lon'):
            continue
            
        try:
            lat = float(school['lat'])
            lon = float(school['lon'])
        except (ValueError, TypeError):
            continue
        
        # Color code: blue for public, red for private
        school_type = str(school.get("type", "")).lower()
        color = "blue" if "public" in school_type else "lightred"
        icon = "graduation-cap"
        
        # Create popup content
        popup_html = f"""
        <div style="font-family: Arial; min-width: 200px; max-width: 300px;">
            <b style="font-size: 14px; color: #2c3e50;">{school.get('name', 'Unknown School')}</b><br>
            <span style="font-size: 12px; color: #7f8c8d;">{school.get('type', 'N/A')}</span><br>
            <span style="font-size: 11px; color: #95a5a6; margin-top: 4px; display: block;">
                Click for details
            </span>
        </div>
        """
        
        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=school.get('name', 'Unknown School'),
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
                if not school.get('lat') or not school.get('lon'):
                    continue
                try:
                    school_lat = float(school['lat'])
                    school_lon = float(school['lon'])
                    if abs(school_lat - clicked_lat) < 0.001 and abs(school_lon - clicked_lng) < 0.001:
                        st.session_state.selected_school = school
                        break
                except (ValueError, TypeError):
                    continue
    
    # Add schools table below the map
    st.markdown("---")
    st.markdown("### 📊 All Schools at a Glance")
    
    # Prepare table data
    table_data = []
    for school in SCHOOLS:
        # Extract screen policy
        screen_policy = school.get("device_policy_summary") or ""
        if screen_policy and len(str(screen_policy)) > 60:
            screen_policy = str(screen_policy)[:60] + "..."
        
        # Extract Micole rating - handle None, empty strings, etc.
        micole_rating = school.get("micole_rating")
        if micole_rating is None or micole_rating == "":
            micole_display = "—"
        else:
            try:
                micole_display = float(micole_rating)
            except (ValueError, TypeError):
                micole_display = "—"
        
        table_data.append({
            "Micole Rating": micole_display,
            "School": school.get("name") or "N/A",
            "Type": school.get("type") or "N/A",
            "Municipality": school.get("municipality") or "N/A",
            "Ages": school.get("ages") or "N/A",
            "Curriculum": school.get("curriculum") or "N/A",
            "Languages": school.get("languages_day_to_day") or "N/A",
            "Screen Policy": screen_policy or "N/A"
        })
    
    df = pd.DataFrame(table_data)
    
    # Sort by Micole Rating (descending), with "—" (no rating) at the bottom
    def sort_key(x):
        if x == "—":
            return -999
        try:
            return float(x)
        except (ValueError, TypeError):
            return -999
    
    df['_sort_key'] = df['Micole Rating'].apply(sort_key)
    df = df.sort_values('_sort_key', ascending=False).drop('_sort_key', axis=1).reset_index(drop=True)
    
    # Display as interactive dataframe
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Micole Rating": st.column_config.TextColumn("⭐ Micole", width="small"),
            "School": st.column_config.TextColumn("School Name", width="large"),
            "Type": st.column_config.TextColumn("Type", width="small"),
            "Municipality": st.column_config.TextColumn("Location", width="small"),
            "Ages": st.column_config.TextColumn("Ages", width="small"),
            "Curriculum": st.column_config.TextColumn("Curriculum", width="medium"),
            "Languages": st.column_config.TextColumn("Languages", width="medium"),
            "Screen Policy": st.column_config.TextColumn("Screen/Device Policy", width="large")
        }
    )

with col2:
    st.markdown("### 📋 School Information")
    
    if st.session_state.selected_school:
        school = st.session_state.selected_school
        
        # School header
        school_name = school.get("name") or "Unknown School"
        school_type = school.get("type") or "N/A"
        st.markdown(f'<div class="school-header">{school_name}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="school-type">{school_type}</div>', unsafe_allow_html=True)
        
        # Special notes at the top as summary
        special_notes = school.get("special_notes")
        if special_notes and str(special_notes).strip():
            st.markdown(f'<div class="info-value" style="background-color: #f0f2f6; padding: 12px; border-radius: 8px; margin: 12px 0; font-size: 0.95em; line-height: 1.5;">{special_notes}</div>', unsafe_allow_html=True)
            st.markdown("---")
        
        # Address & Municipality
        st.markdown('<div class="info-label">📍 Location</div>', unsafe_allow_html=True)
        address = school.get("address") or "Address not available"
        municipality = school.get("municipality") or ""
        neighborhood = school.get("neighborhood") or ""
        location_parts = [address]
        if neighborhood:
            location_parts.append(f"<i>{neighborhood}</i>")
        if municipality:
            location_parts.append(f"<b>{municipality}</b>")
        st.markdown(f'<div class="info-value">{"<br>".join(location_parts)}</div>', unsafe_allow_html=True)
        
        # Founded
        founded = school.get("founded")
        if founded:
            st.markdown('<div class="info-label">📅 Founded</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{founded}</div>', unsafe_allow_html=True)
        
        # Student Count
        student_count = school.get("student_count")
        if student_count and str(student_count).strip():
            st.markdown('<div class="info-label">👥 Students</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{student_count}</div>', unsafe_allow_html=True)
        
        # Ages & Stages
        ages = school.get("ages")
        if ages and str(ages).strip():
            st.markdown('<div class="info-label">👶 Ages</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{ages}</div>', unsafe_allow_html=True)
        
        stages = school.get("stages")
        if stages and str(stages).strip():
            st.markdown('<div class="info-label">🎓 Stages</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{stages}</div>', unsafe_allow_html=True)
        
        # Curriculum
        curriculum = school.get("curriculum")
        if curriculum and str(curriculum).strip():
            st.markdown('<div class="info-label">📚 Curriculum</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{curriculum}</div>', unsafe_allow_html=True)
        
        # Languages
        languages_display = school.get("languages_day_to_day") or ""
        if languages_display and str(languages_display).strip():
            st.markdown('<div class="info-label">🌐 Languages (Day-to-Day)</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{languages_display}</div>', unsafe_allow_html=True)
        
        languages_taught = school.get("languages_taught") or ""
        if languages_taught and str(languages_taught).strip():
            st.markdown('<div class="info-label">🗣️ Languages Taught</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{languages_taught}</div>', unsafe_allow_html=True)
        
        # Screen/Device Policy
        device_policy = school.get("device_policy_summary") or ""
        if device_policy and str(device_policy).strip():
            st.markdown('<div class="info-label">💻 Device Policy</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{device_policy}</div>', unsafe_allow_html=True)
        
        # Pedagogy
        pedagogy = school.get("pedagogy")
        if pedagogy and str(pedagogy).strip():
            st.markdown('<div class="info-label">🎯 Pedagogy</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{pedagogy}</div>', unsafe_allow_html=True)
        
        # Fees
        fees_range = school.get("fees_range")
        if fees_range and str(fees_range).strip():
            st.markdown('<div class="info-label">💰 Fees</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{fees_range}</div>', unsafe_allow_html=True)
        
        # Reviews
        review_parts = []
        google_rating = school.get("google_rating")
        google_reviews = school.get("google_reviews")
        micole_rating = school.get("micole_rating")
        micole_reviews = school.get("micole_reviews")
        
        if google_rating:
            reviews_text = f" ({google_reviews} reviews)" if google_reviews else ""
            review_parts.append(f"Google: {google_rating}⭐{reviews_text}")
        if micole_rating:
            reviews_text = f" ({micole_reviews} reviews)" if micole_reviews else ""
            review_parts.append(f"Micole: {micole_rating}⭐{reviews_text}")
        
        if review_parts:
            st.markdown('<div class="info-label">⭐ Reviews</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{" | ".join(review_parts)}</div>', unsafe_allow_html=True)
        
        st.divider()
        
        # Google Maps link
        lat = school.get('lat')
        lon = school.get('lon')
        if lat and lon:
            try:
                gmaps_url = f"https://www.google.com/maps/search/?api=1&query={float(lat)},{float(lon)}"
                st.markdown(f"[🗺️ Open in Google Maps]({gmaps_url})")
            except (ValueError, TypeError):
                pass
        
    else:
        st.info("👆 Click a school pin on the map to view details")
        
        # Show school count
        st.divider()
        st.metric("Total Schools", len(SCHOOLS))
        
        public_count = sum(1 for s in SCHOOLS if s.get("type") and "public" in str(s.get("type", "")).lower())
        private_count = len(SCHOOLS) - public_count
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Public", public_count)
        with col_b:
            st.metric("Private", private_count)
