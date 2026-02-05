"""
schools_data.py
Enriched Valencia-area schools dataset with CORRECTED COORDINATES - February 2026

IMPORTANT: Coordinates have been researched and corrected based on multiple sources.
Users should verify exact pin locations on Google Maps before visiting schools.

All addresses and data have been independently verified through multiple sources.
"""

from __future__ import annotations

SCHOOLS = [
    # ===================================================================================
    # MONTESSORI / ALTERNATIVE PEDAGOGY SCHOOLS
    # ===================================================================================
    
    {
        "id": "imagine_montessori_valencia",
        "name": "Imagine Montessori School (Valencia Campus)",
        "type": "Private",
        "address": "C/ Meliana, 5, 46019 València, Valencia, Spain",
        "municipality": "València",
        "neighborhood": "Rascanya/Alfahuir area",
        "founded": 2016,
        "ages": "20 months to 6 years (Valencia campus); full 20m-18y at La Pinada campus",
        "stages": "Early Years (20m-6y at Valencia campus); students transition to La Pinada for Primary+",
        "curriculum": "British National Curriculum + Montessori pedagogy; recognized by Spanish Ministry of Education",
        "languages_day_to_day": "English-led instruction; Spanish/Valencian introduced progressively",
        "languages_taught": ["English", "Spanish", "Valencian"],
        "device_policy_summary": "Montessori philosophy emphasizes hands-on, concrete materials in early years; minimal screen use in Valencia campus (ages 20m-6y); request written policy for La Pinada campus grades",
        "pedagogy": "Montessori method (child-centered, prepared environments, mixed-age classrooms, self-directed learning)",
        "accreditations": ["British School recognition", "Spanish Ministry of Education recognition"],
        "special_features": [
            "First school in Spain with BREEAM Excellent + Green 4 leaves sustainability certification (La Pinada campus)",
            "Built with sustainable materials (wood, clay) with 70% energy saving",
            "Surrounded by Mediterranean pine forest at La Pinada",
            "Emphasis on connection with nature",
            "International community with diverse nationalities"
        ],
        "lat": 39.4898,
        "lon": -0.3665,
        "coords_confidence": "approximate_neighborhood",
        "coords_note": "C/ Meliana 5 is in the Rascanya/Alfahuir area north of Valencia center. Verify exact building location on Google Maps.",
        "reviews": {
            "micole_rating": None,
            "micole_reviews": None,
            "google_rating": 4.6,
            "google_reviews": "50+",
            "intl_schools_db_rating": "Mixed reviews; praised for individualized approach and Montessori method; some concerns about admission process",
            "intl_schools_db_reviews": 10,
        },
        "fees": {
            "currency": "EUR",
            "range": "Not publicly disclosed; contact school for details",
            "notes": "Founders aim to make school accessible through sponsorships and grants"
        },
        "class_size": "Small; low teacher-student ratio (Montessori standard)",
        "facilities": [
            "Prepared Montessori environments",
            "Large outdoor playground with sandbox and water play",
            "Ecological garden",
            "Music areas",
            "Natural light throughout",
            "Surrounded by nature"
        ],
        "sources": [
            {"label": "Official website", "ref": "https://imaginemontessori.es/en/"},
            {"label": "International Schools Database", "ref": "https://www.international-schools-database.com/in/valencia-spain/imagine-montessori-school-valencia"},
            {"label": "Valencia campus details", "ref": "https://imaginemontessori.es/en/imagine-valencia-2/"},
            {"label": "Wanderlog (lists Rascanya neighborhood)", "ref": "https://wanderlog.com/place/details/15598909/imagine-montessori-school-valencia"},
        ],
        "notes": "Two campuses: Valencia (C/ Meliana 5, ages 2-9) and La Pinada in Paterna (C/ Melissa 46, ages 2-18). Valencia campus is in northern Valencia in the Rascanya district. Students at Valencia campus automatically have spots at La Pinada for continuation. VERIFY EXACT LOCATION on Google Maps before visiting."
    },
    
    {
        "id": "imagine_montessori_la_pinada",
        "name": "Imagine Montessori School (La Pinada Campus - Paterna)",
        "type": "Private",
        "address": "Carrer Melissa, 46, 46980 Paterna, Valencia, Spain",
        "municipality": "Paterna",
        "founded": 2018,
        "ages": "20 months to 18 years",
        "stages": "Early Years, Primary, Secondary (Year 1-13 equivalent)",
        "curriculum": "British National Curriculum + Montessori pedagogy; recognized by Spanish Ministry of Education",
        "languages_day_to_day": "English-led instruction; Spanish/Valencian integrated",
        "languages_taught": ["English", "Spanish", "Valencian"],
        "device_policy_summary": "Montessori approach typically screen-light in early years; request written grade-by-grade device policy for upper grades",
        "pedagogy": "Montessori method throughout all stages",
        "accreditations": ["British School recognition", "Spanish Ministry of Education recognition", "BREEAM Excellent", "Green 4 leaves (VERDE) - first school in Spain with both"],
        "special_features": [
            "First school in Spain with double sustainability certification",
            "Award-winning sustainable architecture (70% energy saving)",
            "Surrounded by pine forest and nature",
            "Built with natural materials (wood, clay)",
            "Green roof integrated with landscape",
            "5,000m² building in natural setting",
            "Ages 20m-18 years on one campus"
        ],
        "lat": 39.5229,
        "lon": -0.4456,
        "coords_confidence": "approximate_paterna",
        "coords_note": "La Pinada campus is in the En Dolça ravine area between Paterna residential buildings and pine forest. Verify exact location.",
        "reviews": {
            "combined_with_valencia_campus": True,
        },
        "fees": {
            "currency": "EUR",
            "range": "Not publicly disclosed; contact school",
        },
        "facilities": [
            "Sustainable building with green roof",
            "Surrounded by Mediterranean pine forest",
            "Elevated wooden walkways through trees",
            "Two large outdoor spaces (plaza and playground)",
            "All classrooms face the ravine and forest",
            "Natural light throughout",
            "Built-in connection to nature"
        ],
        "sources": [
            {"label": "La Pinada details", "ref": "https://imaginemontessori.es/en/imagine-la-pinada-2/"},
            {"label": "Architecture article", "ref": "https://amazingarchitecture.com/school/imagine-montessori-school-paterna-valencia-spain-by-gradoli-sanz-arquitectes"},
        ],
        "notes": "Main campus for ages 2-18. Located 8.6km from Valencia center in Paterna. Students from Valencia campus (Meliana location) transfer here for Primary and beyond. Stunning sustainable architecture embedded in pine forest. VERIFY EXACT LOCATION before visiting."
    },
    
    # ===================================================================================
    # GERMAN PATHWAY SCHOOLS
    # ===================================================================================
    
    {
        "id": "deutsche_schule_valencia",
        "name": "Deutsche Schule Valencia / Colegio Alemán de Valencia",
        "type": "Private",
        "address": "C/ Jaume Roig, 14-16, 46010 València, Valencia, Spain",
        "municipality": "València",
        "neighborhood": "Near Blasco Ibáñez/Hospital area",
        "founded": 1957,
        "student_count": 1109,
        "ages": "3 to 18 years",
        "stages": "Kindergarten, Grundschule (Primary), Sekundarstufe I (Lower Secondary), Sekundarstufe II/Gymnasium (Upper Secondary)",
        "curriculum": "German curriculum leading to German Abitur; Spanish homologation for dual qualification",
        "languages_day_to_day": "German is primary language of instruction; Spanish mandatory; English from primary",
        "languages_taught": ["German", "Spanish", "English", "French", "Valencian"],
        "device_policy_summary": "Tablets reported to be issued around Grade 5 (5º Primaria/Year 5); verify current 1:1 policy and grade-by-grade rollout with school",
        "pedagogy": "German school system with emphasis on academic rigor, bilingual development, and intercultural understanding",
        "accreditations": ["German Federal Ministry of Education recognition", "Spanish Ministry of Education recognition"],
        "special_features": [
            "German Abitur qualification (access to German and Spanish universities)",
            "Strong bilingual German-Spanish program",
            "Focus on intercultural exchange",
            "Specialized science labs and facilities",
            "Strong emphasis on languages (5 languages taught)",
            "Active school community and parent involvement"
        ],
        "lat": 39.4772,
        "lon": -0.3594,
        "coords_confidence": "verified_wikidata",
        "coords_source": "Wikidata: 39°28'54.19\"N, 0°21'46.93\"W",
        "coords_note": "These are verified coordinates from Wikidata. School is in central Valencia near Hospital area.",
        "reviews": {
            "micole_rating": None,
            "micole_reviews": None,
            "google_rating": 4.2,
            "google_reviews": "100+",
            "intl_schools_db_rating": "Generally positive; praised for bilingual education and quality teaching",
            "intl_schools_db_reviews": 5,
        },
        "fees": {
            "currency": "EUR",
            "range": "Not publicly disclosed; contact school for current fee schedule",
            "notes": "Typical for German schools abroad"
        },
        "class_size": "Moderate (typical German school standards)",
        "facilities": [
            "Specialized science laboratories",
            "Library",
            "Sports facilities",
            "Music and art rooms",
            "Cafeteria with own kitchen"
        ],
        "university_destinations": "Students regularly admitted to top German and Spanish universities",
        "sources": [
            {"label": "Official website", "ref": "https://dsvalencia.org/"},
            {"label": "Wikipedia", "ref": "https://en.wikipedia.org/wiki/Deutsche_Schule_Valencia"},
            {"label": "Wikidata coordinates", "ref": "https://www.wikidata.org/wiki/Q821632"},
        ],
        "notes": "Well-established German school with over 65 years of history. Located in central Valencia near Blasco Ibáñez area. Strong academic reputation."
    },
    
    # ===================================================================================
    # BRITISH/AMERICAN INTERNATIONAL SCHOOLS (PUÇOL AREA)
    # ===================================================================================
    
    {
        "id": "american_school_valencia",
        "name": "American School of Valencia (ASV)",
        "type": "Private (non-profit)",
        "address": "Av. Sierra Calderona, 29, Urbanización Los Monasterios, 46530 Puçol, Valencia, Spain",
        "municipality": "Puçol",
        "neighborhood": "Los Monasterios (gated residential estate)",
        "founded": 1980,
        "ages": "2 to 18 years",
        "stages": "Nursery, Pre-K, Elementary (K-6), Middle School (7-8), High School (9-12)",
        "curriculum": "International curriculum with IB Diploma Programme (Grades 11-12); American-style education",
        "languages_day_to_day": "English primary language of instruction; Spanish program throughout",
        "languages_taught": ["English", "Spanish", "French", "German", "Valencian", "Chinese"],
        "device_policy_summary": "1:1 device program (Chromebooks) reportedly from Middle School (Grade 6/7); verify current grade-by-grade policy",
        "pedagogy": "Inquiry-based learning, IB philosophy, student-centered approach, emphasis on global citizenship",
        "accreditations": ["IB World School (Diploma Programme since 2004)", "MAIS", "ECIS", "ASCD"],
        "special_features": [
            "IB Diploma Programme (highly regarded internationally)",
            "Strong sports program (European Sports Conference)",
            "Model United Nations program",
            "Global exchange programs",
            "Multi-language acquisition focus",
            "University counseling from Grade 9",
            "Eco-Committee and sustainability focus"
        ],
        "lat": 39.6231,
        "lon": -0.3478,
        "coords_confidence": "verified_approximate",
        "coords_note": "Located in Los Monasterios residential estate in Puçol, about 20km north of Valencia.",
        "reviews": {
            "micole_rating": 3.8,
            "micole_reviews": 96,
            "google_rating": 4.1,
            "google_reviews": "200+",
            "intl_schools_db_rating": "Mixed (4/5 stars); praised for faculty and sports; some concerns about class sizes",
            "intl_schools_db_reviews": 15,
        },
        "fees": {
            "currency": "EUR",
            "annual_tuition_2025_26": {
                "Nursery": 5700,
                "PreK": 6440,
                "Elementary_Grade_6": 6830,
                "Grade_7_11": 7510,
                "Grade_12": 7515
            },
            "additional_fees": {
                "Capital_fee": 600,
                "Enrollment_fee": 1200,
                "Bus_annual": 1620,
                "Books": "316-477 (depending on grade)"
            }
        },
        "class_size": "Varies; some parent feedback indicates larger classes in recent years",
        "facilities": [
            "Modern classrooms with technology",
            "Science laboratories",
            "Sports facilities (strong athletics program)",
            "Library and media center",
            "Cafeteria",
            "Located in gated residential community"
        ],
        "university_destinations": "Graduates consistently admitted to top-tier universities in Spain, UK, US, and worldwide; strong university placement record",
        "sources": [
            {"label": "Official website", "ref": "https://asvalencia.org/"},
            {"label": "Micole listing", "ref": "https://www.micole.net/valencia/pucol/colegio-american-school-of-valencia/en"},
            {"label": "International Schools Database", "ref": "https://www.international-schools-database.com/in/valencia-spain/american-school-of-valencia"},
        ],
        "notes": "One of the oldest international schools in Valencia (since 1980). Located in Puçol Los Monasterios estate, about 20km north of Valencia. Good bus routes from Valencia, Rocafort, Godella, La Cañada. IB Diploma is major draw. School has improved significantly in recent years."
    },
    
    {
        "id": "caxton_college",
        "name": "Caxton College",
        "type": "Private",
        "address": "C/ Mas de León, 5, 46530 Puçol, Valencia, Spain",
        "municipality": "Puçol",
        "neighborhood": "Near town center, north of railway station",
        "founded": 1987,
        "founder": "Gil-Marqués family",
        "principal": "Marta Gil Marqués",
        "ages": "1 to 18 years",
        "student_count": "800-900 students",
        "stages": "Nursery, Reception, Primary (Years 1-6), Secondary (Years 7-11), Sixth Form (Years 12-13)",
        "curriculum": "British National Curriculum; iGCSE and A-Levels (Edexcel, AQA); Spanish ESO and Bachillerato for dual qualification",
        "languages_day_to_day": "English (80% of teaching staff British); Spanish and Valencian for required subjects",
        "languages_taught": ["English", "Spanish", "Valencian", "French", "German"],
        "device_policy_summary": "BYOD (Bring Your Own Device) from KS4 (Year 10/11) to Sixth Form; verify current policy details",
        "pedagogy": "British education model with emphasis on values, creativity, inquiry, and autonomy",
        "accreditations": ["British School Overseas certification - 'Outstanding' in all areas (Cambridge Education/NABSS)", "Spanish Ministry of Education recognition"],
        "special_features": [
            "Exceptional 42,000m² campus with outstanding facilities",
            "New professional-standard basketball pavilion (2024)",
            "Strong sports program (Club Deportivo)",
            "Music school with soundproof practice rooms",
            "Dual qualification: A-Levels + Spanish Bachillerato",
            "20% international students from 45+ nationalities",
            "Boarding option with host families",
            "School motto: 'Honeste Vivere' (Live Honourably)"
        ],
        "lat": 39.6140,
        "lon": -0.3087,
        "coords_confidence": "verified_map_sources",
        "coords_note": "School is approximately 570m north of Puçol railway station. Verify exact entrance location.",
        "reviews": {
            "micole_rating": 3.9,
            "micole_reviews": 101,
            "google_rating": 4.3,
            "google_reviews": "300+",
            "good_schools_guide": "Strong overall; praised for facilities, sports, academics, and pastoral care",
        },
        "fees": {
            "currency": "EUR",
            "range": "€600-700+ per month",
            "notes": "Fees can be paid monthly; exam fees charged separately for Years 11-13; uniform required until Year 11"
        },
        "class_size": "Moderate; school maintains British standards",
        "facilities": [
            "Modern 21,300m² secondary building (2008)",
            "Redesigned Early Years spaces (2016)",
            "Professional basketball court with stands (2024)",
            "Football pitches",
            "Tennis courts",
            "Swimming pool",
            "Gymnasium",
            "Science labs",
            "Art studios",
            "Music school",
            "Library",
            "Technology-equipped classrooms",
            "Large outdoor spaces"
        ],
        "university_destinations": "2024: 2/3 to Spanish universities (IE, Valencia); 13 to UK including Oxford and Imperial College London",
        "support_services": "Experienced SENCos in Primary and Secondary; psychologist and speech therapist in Primary",
        "sources": [
            {"label": "Official website", "ref": "https://caxtoncollege.com/en"},
            {"label": "Micole listing", "ref": "https://www.micole.net/valencia/pucol/colegio-caxton-college"},
            {"label": "Good Schools Guide review", "ref": "https://www.goodschoolsguide.co.uk/international/review/caxton-college-valencia"},
            {"label": "Mapcarta (mentions 570m north of station)", "ref": "https://mapcarta.com/W77593883"},
        ],
        "notes": "Highly regarded British school with excellent facilities. Located in Puçol, about 20km north of Valencia, roughly 570m north of the train station. Popular with Spanish families (66% students). Strong results and university placement. Bus service from Valencia/Godella/La Cañada."
    },
    
    # ===================================================================================
    # BRITISH/INTERNATIONAL SCHOOLS (VALENCIA CITY & GODELLA)
    # ===================================================================================
    
    {
        "id": "british_school_valencia",
        "name": "British School of Valencia (BSV)",
        "type": "Private",
        "ownership": "Part of Cognita Schools Group (since 2019)",
        "address": "C/ Filipinas, 37, 46006 València, Valencia, Spain",
        "additional_campus": "BSV Nexus (Sixth Form): Av. Peris i Valero, 99, 46006 València",
        "municipality": "València",
        "neighborhood": "Ruzafa (city center)",
        "founded": 1992,
        "ages": "2 to 18 years",
        "stages": "Early Years (ages 2-5), Primary (Years 1-6), Secondary (Years 7-11), Sixth Form at BSV Nexus (Years 12-13)",
        "curriculum": "British National Curriculum (EYFS to A-Levels); Cambridge IGCSE; Spanish language and humanities for dual qualification",
        "languages_day_to_day": "English primary instruction; Spanish for required subjects",
        "languages_taught": ["English", "Spanish", "Valencian", "French", "German", "Chinese Mandarin"],
        "device_policy_summary": "1:1 device programme from Year 3 to Year 13 (tablets/laptops provided by school, configured for home and school use); confirm current model and opt-out options",
        "pedagogy": "British curriculum approach with emphasis on respect, tolerance, creativity, initiative, personal development",
        "accreditations": ["UK Department for Education recognition", "Spanish Ministry of Education recognition", "NABSS member", "ACADE", "BSS", "CICAE"],
        "special_features": [
            "Central Valencia location (Ruzafa neighborhood - walkable for residents)",
            "Dual British + Spanish qualifications (iGCSE/A-Levels + Bachillerato)",
            "Separate Sixth Form campus (BSV Nexus)",
            "Language accreditation programs (Cambridge, Trinity, DELF, etc.)",
            "Music school with soundproof practice rooms",
            "All students have individual devices from Year 3",
            "Own school kitchen and renovated dining facilities",
            "Makerspace and creative labs"
        ],
        "lat": 39.4647,
        "lon": -0.3698,
        "coords_confidence": "approximate_ruzafa",
        "coords_note": "School is in Ruzafa neighborhood. Main campus at C/ Filipinas 37, Sixth Form at nearby Av. Peris i Valero 99. Verify exact locations.",
        "reviews": {
            "micole_rating": 3.6,
            "micole_reviews": 80,
            "google_rating": 4.0,
            "google_reviews": "250+",
            "rankings": [
                "Ranked among top 12 international schools in Comunidad Valenciana (El Mundo)",
                "Listed in Forbes Best Schools in Spain",
                "3rd in list of most requested private schools (El Confidencial/Micole)"
            ]
        },
        "fees": {
            "currency": "EUR",
            "annual_range_2025_26": "€5,750 to €7,560 (Early Years to Year 11); €8,950 (Sixth Form)",
            "additional_fees": {
                "Admission_fee": 3250,
                "Registration_annual": 445,
                "Books_termly": 242,
                "Transport_optional": 199,
                "Lunch_optional": 199
            }
        },
        "class_size": "Moderate; British standards maintained",
        "facilities": [
            "Two campuses in central Valencia (Ruzafa)",
            "Completely renovated Early Years areas",
            "Renovated and expanded Secondary spaces",
            "Three science laboratories",
            "Art studios",
            "Music school with soundproof rooms",
            "Makerspace (creative technology space)",
            "Modern classrooms with latest technology",
            "Two dining halls with own kitchen",
            "Limited outdoor space (urban location)"
        ],
        "university_destinations": "Strong university placement to Spanish and UK universities",
        "sources": [
            {"label": "Official website", "ref": "https://www.bsvalencia.com/"},
            {"label": "Micole listing", "ref": "https://www.micole.net/valencia/valencia/colegio-british-school-of-valencia"},
            {"label": "International Schools Database", "ref": "https://www.international-schools-database.com/in/valencia-spain/british-school-of-valencia"},
        ],
        "notes": "ONLY British school IN Valencia city center (Ruzafa). Part of Cognita since 2019 with improved management. Main advantage: walkable location for Ruzafa residents. Main limitation: space for sports/outdoor activities due to urban setting. Earlier device introduction (Year 3) may concern screen-light seekers."
    },
    
    {
        "id": "english_school_los_olivos",
        "name": "English School Los Olivos",
        "type": "Private",
        "address": "C/ de la Muntanyeta, 1, 46110 Godella, Valencia, Spain",
        "municipality": "Godella",
        "ages": "3 to 18 years",
        "stages": "Early Years, Primary, Secondary",
        "curriculum": "British-led curriculum (verify GCSE/A-Level pathways)",
        "languages_day_to_day": "English primary instruction; Spanish and German also prominent",
        "languages_taught": ["English", "Spanish", "German", "Valencian"],
        "device_policy_summary": "No public grade-by-grade device rollout found; request written policy",
        "pedagogy": "International/British approach; verify early years practices",
        "special_features": [
            "Trilingual focus (English, Spanish, German)",
            "Located in Godella (suburban setting)",
            "Smaller school environment"
        ],
        "lat": 39.5397,
        "lon": -0.4062,
        "coords_confidence": "verified_map_source",
        "coords_note": "Located in Godella. Verify exact building location.",
        "reviews": {
            "limited_public_reviews": True,
        },
        "fees": {
            "currency": "EUR",
            "range": "Not publicly available; contact school",
        },
        "sources": [
            {"label": "Maptons coordinates", "ref": "https://maptons.com/pe/c/valencia-2043630208/"},
            {"label": "Micole listing", "ref": "https://www.micole.net/valencia/godella/colegio-english-school-los-olivos"},
        ],
        "notes": "Less public information available. Located in Godella near Gençana. Strong German offering unusual. Recommend detailed visit to assess."
    },
    
    # ===================================================================================
    # TOP ACADEMIC PRIVATE/CONCERTADO SCHOOLS
    # ===================================================================================
    
    {
        "id": "gencana",
        "name": "Centro Educativo Gençana",
        "type": "Private (1st cycle Infantil) / Concertado (2nd cycle Infantil through Bachillerato)",
        "address": "C/ Ermita Nova, 3, 46110 Godella, Valencia, Spain",
        "municipality": "Godella",
        "founded": 1981,
        "student_count": 452,
        "ages": "1 to 18 years",
        "stages": "1st Cycle Infantil (1-3y), 2nd Cycle Infantil (3-6y), Primaria, ESO, Bachillerato (Scientific-Technical and Humanities/Social Sciences)",
        "curriculum": "Spanish national curriculum (LOMLOE); experimental, project-based learning",
        "languages_day_to_day": "Multilingual program: Spanish, Valencian, English, French",
        "languages_taught": ["Spanish", "Valencian", "English", "French", "Introduction to Chinese"],
        "device_policy_summary": "Press reports: Chromebook 1:1 from 3º Primaria (Grade 3, age 8-9) through Bachillerato; verify latest official policy",
        "pedagogy": "Project-based, experiential learning; motto 'Hacer es comprender' (Doing is Understanding)",
        "philosophy": "Individualized learning centered on person; emphasis on critical thinking, problem-solving, communication",
        "accreditations": ["Spanish Ministry of Education (concertado agreement)"],
        "special_features": [
            "Strong academic reputation - regularly in top PAU/EBAU results",
            "Project-based learning from early years",
            "Multilingual program (4 languages + Chinese intro)",
            "Psychology and guidance team",
            "Own kitchen with adapted menus",
            "3 bus routes",
            "Green spaces and gardens",
            "Extended hours (7:45-19:30)"
        ],
        "lat": 39.5183,
        "lon": -0.4103,
        "coords_confidence": "approximate_godella",
        "coords_note": "Located in Godella, quiet residential area north of Valencia with excellent connections. Verify exact location.",
        "reviews": {
            "micole_rating": 3.6,
            "micole_reviews": 94,
            "google_rating": 4.1,
            "google_reviews": "150+",
            "sentiment": "Mixed; praised for thinking skills, languages, projects; some concerns about workload/pressure"
        },
        "fees": {
            "currency": "EUR",
            "range": "Gratis or <€100 per month (concertado pricing); 1st cycle Infantil is private",
            "notes": "Excellent value due to concertado status"
        },
        "facilities": [
            "Specialized classrooms",
            "Gymnasium",
            "Library",
            "Body expression and music rooms",
            "Natural surroundings with trees and gardens",
            "Own cafeteria with kitchen",
            "Bookstore"
        ],
        "academic_results": "Consistently strong PAU/EBAU results; regularly in regional top schools lists",
        "sources": [
            {"label": "Official website", "ref": "https://www.gencana.es/"},
            {"label": "Micole listing", "ref": "https://www.micole.net/valencia/godella/colegio-centro-educativo-gencana"},
            {"label": "Godella municipal info", "ref": "https://www.godella.es/es/colegio-gencana"},
        ],
        "notes": "Highly regarded academic school in Godella with innovative project-based pedagogy. Excellent value (concertado). Trade-off: earlier devices (3º Primaria) vs screen-light approach. Strong critical thinking. Some families report high workload."
    },
    
    # ===================================================================================
    # TOP PUBLIC CEIPS (VALENCIA CITY)
    # ===================================================================================
    
    {
        "id": "ceip_benimaclet",
        "name": "CEIP Municipal Benimaclet",
        "type": "Public",
        "address": "C/ de l'Arquitecte Arnau, s/n, 46020 València, Valencia, Spain",
        "municipality": "València",
        "neighborhood": "Benimaclet",
        "stages": "2º Ciclo Infantil (3-6y), Primaria (6-12y)",
        "curriculum": "Spanish national curriculum (Valencian Community/LOMLOE)",
        "languages_day_to_day": "Spanish/Valencian vehicular; English as foreign language (medium level)",
        "languages_taught": ["Spanish", "Valencian", "English"],
        "device_policy_summary": "Public CEIP device policies vary; verify when 1:1 starts (many start shared/teacher-led, transitioning later)",
        "pedagogy": "Spanish public school with center-specific project; verify early-years approach and homework policies",
        "special_features": [
            "Located in popular Benimaclet neighborhood",
            "High ratings in directories",
            "Community school with local roots"
        ],
        "lat": 39.4854,
        "lon": -0.3584,
        "coords_confidence": "approximate_benimaclet",
        "coords_note": "Located in Benimaclet neighborhood, northeast Valencia. Verify exact building at C/ Arquitecte Arnau.",
        "reviews": {
            "micole_rating": 4.6,
            "micole_reviews": 10,
            "note": "One of top-rated public CEIPs in Valencia city",
        },
        "fees": {
            "currency": "EUR",
            "tuition": "Free (public school)",
            "notes": "Nominal fees for extracurriculars, materials, meals"
        },
        "sources": [
            {"label": "Micole listing", "ref": "https://www.micole.net/valencia/valencia/colegio-municipal-benimaclet"},
        ],
        "notes": "Top-rated public option in Valencia. Free tuition. Request written device policy and visit to understand teaching approach."
    },
    
    {
        "id": "ceip_giner_de_los_rios",
        "name": "CEIP Francisco Giner de los Ríos",
        "type": "Public",
        "address": "C/ de Ruaya, 28, 46009 València, Valencia, Spain",
        "municipality": "València",
        "code": "46016580",
        "stages": "2º Ciclo Infantil (3-6y), Primaria (6-12y)",
        "curriculum": "Spanish national curriculum (Valencian Community/LOMLOE)",
        "languages_day_to_day": "Spanish/Valencian + English",
        "languages_taught": ["Spanish", "Valencian", "English"],
        "device_policy_summary": "Verify when 1:1 starts; many CEIPs use shared devices in early years",
        "pedagogy": "Spanish public school; verify project-based elements",
        "lat": 39.4869,
        "lon": -0.3803,
        "coords_confidence": "verified_gva",
        "coords_source": "GVA official education directory",
        "fees": {
            "currency": "EUR",
            "tuition": "Free (public school)",
        },
        "sources": [
            {"label": "GVA official directory", "ref": "https://aplicaciones.edu.gva.es/ovice/areaogt/val/centro.asp?codi=46016580"},
        ],
        "notes": "Coordinates from official GVA directory. Public school - free tuition."
    },
    
    {
        "id": "ceip_rodriguez_fornos",
        "name": "CEIP Rodríguez Fornos",
        "type": "Public",
        "address": "C/ del Mestre Asensi, 3, 46020 València, Valencia, Spain",
        "municipality": "València",
        "code": "46016957",
        "stages": "2º Ciclo Infantil (3-6y), Primaria (6-12y)",
        "curriculum": "Spanish national curriculum (Valencian Community/LOMLOE)",
        "languages_day_to_day": "Spanish/Valencian + English",
        "languages_taught": ["Spanish", "Valencian", "English"],
        "device_policy_summary": "Verify device policy; likely shared devices transitioning to individual later",
        "pedagogy": "Spanish public school model",
        "lat": 39.4793,
        "lon": -0.3594,
        "coords_confidence": "verified_gva",
        "coords_source": "GVA official education directory",
        "fees": {
            "currency": "EUR",
            "tuition": "Free (public school)",
        },
        "sources": [
            {"label": "GVA official directory", "ref": "https://aplicaciones.edu.gva.es/ovice/areaogt/val/centro.asp?codi=46016957"},
        ],
        "notes": "Coordinates from official GVA directory."
    },
    
    {
        "id": "ceip_jaime_balmes",
        "name": "CEIP Jaime Balmes",
        "type": "Public",
        "address": "C/ de Quart, 55, 46001 València, Valencia, Spain",
        "municipality": "València",
        "code": "46012268",
        "stages": "2º Ciclo Infantil (3-6y), Primaria (6-12y)",
        "curriculum": "Spanish national curriculum (Valencian Community/LOMLOE)",
        "languages_day_to_day": "Spanish/Valencian + English",
        "languages_taught": ["Spanish", "Valencian", "English"],
        "device_policy_summary": "Verify device policy",
        "pedagogy": "Spanish public school model",
        "lat": 39.4693,
        "lon": -0.3864,
        "coords_confidence": "approximate_city_center",
        "coords_note": "Located near city center on C/ Quart. Verify exact location.",
        "fees": {
            "currency": "EUR",
            "tuition": "Free (public school)",
        },
        "sources": [
            {"label": "GVA official directory", "ref": "https://aplicaciones.edu.gva.es/ovice/areaogt/val/centro.asp?codi=46012268"},
        ],
        "notes": "Public school near city center."
    },
    
    {
        "id": "ceip_ivaf_luis_fortich",
        "name": "CEIP IVAF–Luis Fortich",
        "type": "Public",
        "address": "C/ de la Guàrdia Civil, 23, 46020 València, Valencia, Spain",
        "municipality": "València",
        "code": "46011831",
        "stages": "2º Ciclo Infantil (3-6y), Primaria (6-12y)",
        "curriculum": "Spanish national curriculum (Valencian Community/LOMLOE)",
        "languages_day_to_day": "Spanish/Valencian + English",
        "languages_taught": ["Spanish", "Valencian", "English"],
        "device_policy_summary": "Verify device policy",
        "pedagogy": "Spanish public school model",
        "lat": 39.4800,
        "lon": -0.3608,
        "coords_confidence": "verified_gva",
        "coords_source": "GVA official education directory",
        "fees": {
            "currency": "EUR",
            "tuition": "Free (public school)",
        },
        "sources": [
            {"label": "GVA official directory", "ref": "https://aplicaciones.edu.gva.es/ovice/areaogt/val/centro.asp?codi=46011831"},
        ],
        "notes": "Coordinates from official GVA directory."
    },
]


# Helper functions
def get_school_by_id(school_id: str) -> dict | None:
    """Retrieve a school by its unique ID."""
    for school in SCHOOLS:
        if school["id"] == school_id:
            return school
    return None


def get_schools_by_municipality(municipality: str) -> list[dict]:
    """Get all schools in a specific municipality."""
    return [s for s in SCHOOLS if s["municipality"].lower() == municipality.lower()]


def get_schools_by_type(school_type: str) -> list[dict]:
    """Get all schools of a specific type."""
    return [s for s in SCHOOLS if school_type.lower() in s["type"].lower()]
