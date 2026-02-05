import streamlit as st
import pandas as pd
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
    
    # Create map with minimal black and white style
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=11,
        tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
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
    
    # Add schools table below the map
    st.markdown("---")
    st.markdown("### 📊 All Schools at a Glance")
    
    # Prepare table data
    table_data = []
    for school in SCHOOLS:
        # Extract screen policy - handle both old and new field names
        screen_policy = school.get("device_policy_summary", school.get("screen_policy", "N/A"))
        if screen_policy and len(screen_policy) > 60:
            screen_policy = screen_policy[:60] + "..."
        
        # Extract Micole rating
        micole_rating = None
        if school.get("reviews") and isinstance(school["reviews"], dict):
            micole_rating = school["reviews"].get("micole_rating")
        
        table_data.append({
            "Micole Rating": micole_rating if micole_rating is not None else "—",
            "School": school.get("name", "N/A"),
            "Type": school.get("type", "N/A"),
            "Municipality": school.get("municipality", "N/A"),
            "Ages": school.get("ages", "N/A"),
            "Curriculum": school.get("curriculum", "N/A"),
            "Languages": school.get("languages_day_to_day", school.get("languages", "N/A")),
            "Screen Policy": screen_policy
        })
    
    df = pd.DataFrame(table_data)
    
    # Sort by Micole Rating (descending), with "—" (no rating) at the bottom
    df['_sort_key'] = df['Micole Rating'].apply(lambda x: -999 if x == "—" else float(x))
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
        st.markdown(f'<div class="school-header">{school.get("name", "Unknown School")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="school-type">{school.get("type", "N/A")}</div>', unsafe_allow_html=True)
        
        # Notes at the top as summary
        if school.get("notes"):
            st.markdown('<div class="info-value" style="background-color: #f0f2f6; padding: 12px; border-radius: 8px; margin: 12px 0; font-size: 0.95em; line-height: 1.5;">{}</div>'.format(school["notes"]), unsafe_allow_html=True)
            st.markdown("---")
        
        # Address & Municipality
        st.markdown('<div class="info-label">📍 Location</div>', unsafe_allow_html=True)
        address = school.get("address", "N/A")
        municipality = school.get("municipality", "")
        if municipality:
            st.markdown(f'<div class="info-value">{address}<br>{municipality}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="info-value">{address}</div>', unsafe_allow_html=True)
        
        # Founded
        if school.get("founded"):
            st.markdown('<div class="info-label">📅 Founded</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["founded"]}</div>', unsafe_allow_html=True)
        
        # Ages & Stages
        if school.get("ages"):
            st.markdown('<div class="info-label">👶 Ages</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["ages"]}</div>', unsafe_allow_html=True)
        
        if school.get("stages"):
            st.markdown('<div class="info-label">🎓 Stages</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["stages"]}</div>', unsafe_allow_html=True)
        
        # Curriculum
        if school.get("curriculum"):
            st.markdown('<div class="info-label">📚 Curriculum</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["curriculum"]}</div>', unsafe_allow_html=True)
        
        # Languages
        languages_display = school.get("languages_day_to_day", school.get("languages", ""))
        if languages_display:
            st.markdown('<div class="info-label">🌐 Languages</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{languages_display}</div>', unsafe_allow_html=True)
        
        # Screen/Device Policy
        device_policy = school.get("device_policy_summary", school.get("screen_policy", ""))
        if device_policy:
            st.markdown('<div class="info-label">💻 Device Policy</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{device_policy}</div>', unsafe_allow_html=True)
        
        # Pedagogy
        if school.get("pedagogy"):
            st.markdown('<div class="info-label">🎯 Pedagogy</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["pedagogy"]}</div>', unsafe_allow_html=True)
        
        # Fees
        if school.get("fees"):
            st.markdown('<div class="info-label">💰 Fees</div>', unsafe_allow_html=True)
            fees = school["fees"]
            if isinstance(fees, dict):
                if "tuition" in fees:
                    st.markdown(f'<div class="info-value">{fees["tuition"]}</div>', unsafe_allow_html=True)
                elif "range" in fees:
                    st.markdown(f'<div class="info-value">{fees["range"]}</div>', unsafe_allow_html=True)
                elif "annual_range_2025_26" in fees:
                    st.markdown(f'<div class="info-value">{fees["annual_range_2025_26"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="info-value">{fees}</div>', unsafe_allow_html=True)
        
        # Reviews (if available)
        if school.get("reviews"):
            reviews = school["reviews"]
            if isinstance(reviews, dict):
                review_parts = []
                if reviews.get("google_rating"):
                    review_parts.append(f"Google: {reviews['google_rating']}⭐")
                if reviews.get("micole_rating"):
                    review_parts.append(f"Micole: {reviews['micole_rating']}⭐")
                if review_parts:
                    st.markdown('<div class="info-label">⭐ Reviews</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="info-value">{" | ".join(review_parts)}</div>', unsafe_allow_html=True)
        
        # Special Features (collapsible)
        if school.get("special_features"):
            with st.expander("✨ Special Features"):
                for feature in school["special_features"]:
                    st.markdown(f"• {feature}")
        
        # Sources
        if school.get("sources"):
            st.markdown('<div class="info-label">🔗 Sources</div>', unsafe_allow_html=True)
            sources = school["sources"]
            if isinstance(sources, list):
                for source in sources:
                    if isinstance(source, dict):
                        label = source.get("label", "Source")
                        ref = source.get("ref", "")
                        if ref:
                            st.markdown(f"- [{label}]({ref})")
                    else:
                        st.markdown(f"- [{source}]({source})")
        
        st.divider()
        
        # Google Maps link
        gmaps_url = f"https://www.google.com/maps/search/?api=1&query={school['lat']},{school['lon']}"
        st.markdown(f"[🗺️ Open in Google Maps]({gmaps_url})")
        
    else:
        st.info("👆 Click a school pin on the map to view details")
        
        # Show school count
        st.divider()
        st.metric("Total Schools", len(SCHOOLS))
        
        public_count = sum(1 for s in SCHOOLS if "public" in s.get("type", "").lower())
        private_count = len(SCHOOLS) - public_count
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Public", public_count)
        with col_b:
            st.metric("Private", private_count)import streamlit as st
import pandas as pd
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
    
    # Create map with minimal black and white style
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=11,
        tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
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
    
    # Add schools table below the map
    st.markdown("---")
    st.markdown("### 📊 All Schools at a Glance")
    
    # Prepare table data
    table_data = []
    for school in SCHOOLS:
        # Extract screen policy - handle both old and new field names
        screen_policy = school.get("device_policy_summary", school.get("screen_policy", "N/A"))
        if screen_policy and len(screen_policy) > 60:
            screen_policy = screen_policy[:60] + "..."
        
        # Extract Micole rating
        micole_rating = None
        if school.get("reviews") and isinstance(school["reviews"], dict):
            micole_rating = school["reviews"].get("micole_rating")
        
        table_data.append({
            "Micole Rating": micole_rating if micole_rating is not None else "—",
            "School": school.get("name", "N/A"),
            "Type": school.get("type", "N/A"),
            "Municipality": school.get("municipality", "N/A"),
            "Ages": school.get("ages", "N/A"),
            "Curriculum": school.get("curriculum", "N/A"),
            "Languages": school.get("languages_day_to_day", school.get("languages", "N/A")),
            "Screen Policy": screen_policy
        })
    
    df = pd.DataFrame(table_data)
    
    # Sort by Micole Rating (descending), with "—" (no rating) at the bottom
    df['_sort_key'] = df['Micole Rating'].apply(lambda x: -999 if x == "—" else float(x))
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
        st.markdown(f'<div class="school-header">{school.get("name", "Unknown School")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="school-type">{school.get("type", "N/A")}</div>', unsafe_allow_html=True)
        
        # Notes at the top as summary
        if school.get("notes"):
            st.markdown('<div class="info-value" style="background-color: #f0f2f6; padding: 12px; border-radius: 8px; margin: 12px 0; font-size: 0.95em; line-height: 1.5;">{}</div>'.format(school["notes"]), unsafe_allow_html=True)
            st.markdown("---")
        
        # Address & Municipality
        st.markdown('<div class="info-label">📍 Location</div>', unsafe_allow_html=True)
        address = school.get("address", "N/A")
        municipality = school.get("municipality", "")
        if municipality:
            st.markdown(f'<div class="info-value">{address}<br>{municipality}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="info-value">{address}</div>', unsafe_allow_html=True)
        
        # Founded
        if school.get("founded"):
            st.markdown('<div class="info-label">📅 Founded</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["founded"]}</div>', unsafe_allow_html=True)
        
        # Ages & Stages
        if school.get("ages"):
            st.markdown('<div class="info-label">👶 Ages</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["ages"]}</div>', unsafe_allow_html=True)
        
        if school.get("stages"):
            st.markdown('<div class="info-label">🎓 Stages</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["stages"]}</div>', unsafe_allow_html=True)
        
        # Curriculum
        if school.get("curriculum"):
            st.markdown('<div class="info-label">📚 Curriculum</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["curriculum"]}</div>', unsafe_allow_html=True)
        
        # Languages
        languages_display = school.get("languages_day_to_day", school.get("languages", ""))
        if languages_display:
            st.markdown('<div class="info-label">🌐 Languages</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{languages_display}</div>', unsafe_allow_html=True)
        
        # Screen/Device Policy
        device_policy = school.get("device_policy_summary", school.get("screen_policy", ""))
        if device_policy:
            st.markdown('<div class="info-label">💻 Device Policy</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{device_policy}</div>', unsafe_allow_html=True)
        
        # Pedagogy
        if school.get("pedagogy"):
            st.markdown('<div class="info-label">🎯 Pedagogy</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="info-value">{school["pedagogy"]}</div>', unsafe_allow_html=True)
        
        # Fees
        if school.get("fees"):
            st.markdown('<div class="info-label">💰 Fees</div>', unsafe_allow_html=True)
            fees = school["fees"]
            if isinstance(fees, dict):
                if "tuition" in fees:
                    st.markdown(f'<div class="info-value">{fees["tuition"]}</div>', unsafe_allow_html=True)
                elif "range" in fees:
                    st.markdown(f'<div class="info-value">{fees["range"]}</div>', unsafe_allow_html=True)
                elif "annual_range_2025_26" in fees:
                    st.markdown(f'<div class="info-value">{fees["annual_range_2025_26"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="info-value">{fees}</div>', unsafe_allow_html=True)
        
        # Reviews (if available)
        if school.get("reviews"):
            reviews = school["reviews"]
            if isinstance(reviews, dict):
                review_parts = []
                if reviews.get("google_rating"):
                    review_parts.append(f"Google: {reviews['google_rating']}⭐")
                if reviews.get("micole_rating"):
                    review_parts.append(f"Micole: {reviews['micole_rating']}⭐")
                if review_parts:
                    st.markdown('<div class="info-label">⭐ Reviews</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="info-value">{" | ".join(review_parts)}</div>', unsafe_allow_html=True)
        
        # Special Features (collapsible)
        if school.get("special_features"):
            with st.expander("✨ Special Features"):
                for feature in school["special_features"]:
                    st.markdown(f"• {feature}")
        
        # Sources
        if school.get("sources"):
            st.markdown('<div class="info-label">🔗 Sources</div>', unsafe_allow_html=True)
            sources = school["sources"]
            if isinstance(sources, list):
                for source in sources:
                    if isinstance(source, dict):
                        label = source.get("label", "Source")
                        ref = source.get("ref", "")
                        if ref:
                            st.markdown(f"- [{label}]({ref})")
                    else:
                        st.markdown(f"- [{source}]({source})")
        
        st.divider()
        
        # Google Maps link
        gmaps_url = f"https://www.google.com/maps/search/?api=1&query={school['lat']},{school['lon']}"
        st.markdown(f"[🗺️ Open in Google Maps]({gmaps_url})")
        
    else:
        st.info("👆 Click a school pin on the map to view details")
        
        # Show school count
        st.divider()
        st.metric("Total Schools", len(SCHOOLS))
        
        public_count = sum(1 for s in SCHOOLS if "public" in s.get("type", "").lower())
        private_count = len(SCHOOLS) - public_count
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Public", public_count)
        with col_b:
            st.metric("Private", private_count)
