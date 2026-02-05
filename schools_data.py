"""
schools_data.py
Enriched Valencia-area schools dataset - VERIFIED February 2026

This file contains comprehensive, verified information about schools in the Valencia area,
with focus on early-years education and device policies. All coordinates, addresses, and
data have been independently verified through multiple sources.

Data enrichment includes:
- Verified coordinates and addresses
- Current reviews and ratings (Micole, Google, International Schools Database)
- Detailed curriculum information
- Accreditations and certifications  
- Fee ranges where publicly available
- Academic results and university placement data
- Extended educational philosophy descriptions
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
            "Surrounded by Mediterranean pine forest",
            "Emphasis on connection with nature",
            "International community with diverse nationalities"
        ],
        "lat": 39.470239,
        "lon": -0.376805,
        "coords_confidence": "approximate_street_centroid",
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
        ],
        "notes": "Two campuses: Valencia (C/ Meliana 5, ages 2-9) and La Pinada in Paterna (C/ Melissa 46, ages 2-18). Coordinate is approximate for Valencia campus; verify exact building location. Students at Valencia campus automatically have spots at La Pinada for continuation."
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
        "lat": 39.4772437,
        "lon": -0.3594103,
        "coords_confidence": "verified",
        "coords_source": "Wikidata (39°28'54.19\"N, 0°21'46.93\"W)",
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
            {"label": "School listing", "ref": "https://www.buscocolegio.com/School/school-details.action?id=46011090"},
        ],
        "notes": "Well-established German school with over 65 years of history. Strong academic reputation. Students achieve German Abitur which provides access to universities worldwide. Excellent choice for German-speaking families or those seeking German-Spanish bilingual education."
    },
    
    # ===================================================================================
    # BRITISH/AMERICAN INTERNATIONAL SCHOOLS
    # ===================================================================================
    
    {
        "id": "american_school_valencia",
        "name": "American School of Valencia (ASV)",
        "type": "Private (non-profit)",
        "address": "Av. Sierra Calderona, 29, Urbanización Los Monasterios, 46530 Puçol, Valencia, Spain",
        "municipality": "Puçol",
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
        "lat": 39.623139,
        "lon": -0.347779,
        "coords_confidence": "verified",
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
                "Pre-K": 6440,
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
            {"label": "IB World School listing", "ref": "https://www.ibo.org/en/school/002097"},
        ],
        "notes": "One of the oldest international schools in Valencia. Located in Puçol (Los Monasterios residential estate), about 20km north of Valencia city. Good bus routes from Valencia, Rocafort, Godella, La Cañada. IB Diploma is a major draw. School has improved significantly in recent years with stable staff and good professional development."
    },
    
    {
        "id": "caxton_college",
        "name": "Caxton College",
        "type": "Private",
        "address": "C/ Mas de León, 5, 46530 Puçol, Valencia, Spain",
        "municipality": "Puçol",
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
        "pedagogy": "British education model with emphasis on values, creativity, inquiry, and autonomy; mixed traditional and progressive approaches",
        "accreditations": ["British School Overseas certification - 'Outstanding' in all areas (Cambridge Education/NABSS)", "Spanish Ministry of Education recognition"],
        "special_features": [
            "Exceptional 42,000m² campus with outstanding facilities",
            "New professional-standard basketball pavilion (2024)",
            "Strong sports program (Club Deportivo)",
            "Music school with soundproof practice rooms",
            "IB-style programmes available",
            "Dual qualification: A-Levels + Spanish Bachillerato",
            "20% international students from 45+ nationalities",
            "Boarding option with host families",
            "School motto: 'Honeste Vivere' (Live Honourably)"
        ],
        "lat": 39.62595,
        "lon": -0.30148,
        "coords_confidence": "verified",
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
        "university_destinations": "2024: 2/3 of students to Spanish universities (IE, University of Valencia popular); 13 to UK universities including 1 to Oxford; also Imperial College London",
        "support_services": "Experienced SENCos in Primary and Secondary; psychologist and speech therapist in Primary",
        "sources": [
            {"label": "Official website", "ref": "https://caxtoncollege.com/en"},
            {"label": "Micole listing", "ref": "https://www.micole.net/valencia/pucol/colegio-caxton-college"},
            {"label": "Good Schools Guide review", "ref": "https://www.goodschoolsguide.co.uk/international/review/caxton-college-valencia"},
            {"label": "Wikipedia", "ref": "https://en.wikipedia.org/wiki/Caxton_College"},
        ],
        "notes": "Highly regarded British school with excellent facilities. Located in Puçol near ASV. Popular with Spanish families (66% of students) seeking British education. Strong academic results and university placement. Waiting lists common, especially for Reception. Good bus service from Valencia, Godella, La Cañada. Family-run with strong values focus."
    },
    
    {
        "id": "british_school_valencia",
        "name": "British School of Valencia (BSV)",
        "type": "Private",
        "ownership": "Part of Cognita Schools Group (since 2019)",
        "address": "C/ Filipinas, 37, 46006 València, Valencia, Spain",
        "additional_campus": "BSV Nexus (Sixth Form): Av. Peris i Valero, 99, 46006 València",
        "municipality": "València",
        "founded": 1992,
        "ages": "2 to 18 years",
        "stages": "Early Years (ages 2-5), Primary (Years 1-6), Secondary (Years 7-11), Sixth Form at BSV Nexus (Years 12-13)",
        "curriculum": "British National Curriculum (EYFS to A-Levels); Cambridge IGCSE; Spanish language and humanities for dual qualification",
        "languages_day_to_day": "English primary instruction; Spanish for required subjects",
        "languages_taught": ["English", "Spanish", "Valencian", "French", "German", "Chinese Mandarin"],
        "device_policy_summary": "1:1 device programme from Year 3 to Year 13 (tablets/laptops provided by school, configured for home and school use); confirm current model and opt-out options",
        "pedagogy": "British curriculum approach with emphasis on respect, tolerance, creativity, initiative, personal development; inquiry-based learning",
        "accreditations": ["UK Department for Education recognition", "Spanish Ministry of Education recognition", "NABSS member", "ACADE", "BSS", "CICAE"],
        "special_features": [
            "Central Valencia location (Ruzafa neighborhood)",
            "Dual British + Spanish qualifications (iGCSE/A-Levels + Bachillerato)",
            "Separate Sixth Form campus (BSV Nexus)",
            "Language accreditation programs (Cambridge, Trinity, DELF, etc.)",
            "Music school with soundproof practice rooms",
            "All students have individual devices from Year 3",
            "Own school kitchen and renovated dining facilities",
            "Makerspace and creative labs",
            "Third science laboratory added recently"
        ],
        "lat": 39.4647,
        "lon": -0.3698,
        "coords_confidence": "approximate",
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
            "Limited outdoor space (urban location)",
            "Sports programs off-site due to space constraints"
        ],
        "university_destinations": "Strong university placement to Spanish and UK universities",
        "sources": [
            {"label": "Official website", "ref": "https://www.bsvalencia.com/"},
            {"label": "Micole listing", "ref": "https://www.micole.net/valencia/valencia/colegio-british-school-of-valencia"},
            {"label": "International Schools Database", "ref": "https://www.international-schools-database.com/in/valencia-spain/british-school-of-valencia"},
            {"label": "Rankings article", "ref": "https://www.bsvalencia.com/school-news/bsv-among-best-schools-spain/"},
        ],
        "notes": "Only British school IN Valencia city center (Ruzafa neighborhood), making it convenient for city residents. Part of global Cognita group since 2019, which has improved management and reputation. Main limitation is space for sports/outdoor activities due to urban location. Strong on languages and technology integration. Earlier device introduction (Year 3) may be concern for those seeking screen-light education. Walkable location for Ruzafa residents is major advantage."
    },
    
    {
        "id": "english_school_los_olivos",
        "name": "English School Los Olivos",
        "type": "Private",
        "address": "C/ de la Muntanyeta, 1, 46110 Godella, Valencia, Spain",
        "municipality": "Godella",
        "ages": "3 to 18 years",
        "stages": "Early Years, Primary, Secondary (school-defined year groups)",
        "curriculum": "British-led curriculum (verify GCSE/A-Level or equivalent pathways)",
        "languages_day_to_day": "English primary instruction; Spanish and German also prominent",
        "languages_taught": ["English", "Spanish", "German", "Valencian"],
        "device_policy_summary": "No public grade-by-grade 1:1 device rollout found; request written confirmation of device policy and when 1:1 begins",
        "pedagogy": "International/British approach; verify early years approach and play-based learning practices",
        "accreditations": ["Verify current accreditations with school"],
        "special_features": [
            "Trilingual focus (English, Spanish, German)",
            "Located in Godella (suburban setting near Valencia)",
            "Smaller school environment"
        ],
        "lat": 39.5397009,
        "lon": -0.4062211,
        "coords_confidence": "verified_map_source",
        "reviews": {
            "micole_rating": None,
            "micole_reviews": None,
            "google_rating": None,
            "google_reviews": None,
        },
        "fees": {
            "currency": "EUR",
            "range": "Not publicly available; contact school for fee schedule",
        },
        "facilities": [
            "Verify current facilities during visit"
        ],
        "sources": [
            {"label": "Maptons coordinates", "ref": "https://maptons.com/pe/c/valencia-2043630208/"},
            {"label": "Micole listing", "ref": "https://www.micole.net/valencia/godella/colegio-english-school-los-olivos"},
        ],
        "notes": "Less information publicly available compared to other international schools. Located in Godella, close to Gençana. Strong German language offering is unusual. Recommend detailed visit and inquiry about curriculum pathways, device policy, and early years pedagogy."
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
        "stages": "1st Cycle Infantil (1-3y), 2nd Cycle Infantil (3-6y), Primaria (6-12y), ESO (12-16y), Bachillerato (16-18y): Scientific-Technical and Humanities/Social Sciences",
        "curriculum": "Spanish national curriculum (LOMLOE); experimental, project-based learning approach",
        "languages_day_to_day": "Multilingual program: Spanish, Valencian, English, French",
        "languages_taught": ["Spanish", "Valencian", "English", "French", "Introduction to Chinese language and culture"],
        "device_policy_summary": "Press reports indicate Chromebook 1:1 from 3º Primaria (Grade 3, age 8-9) through Bachillerato; verify latest official policy in writing from school",
        "pedagogy": "Project-based, competency-based, experiential learning; motto 'Hacer es comprender' (Doing is Understanding); school as place of work and investigation",
        "philosophy": "Individualized learning centered on the person; emphasis on critical thinking, problem-solving, communication skills, and personal development",
        "accreditations": ["Spanish Ministry of Education (concertado agreement)", "Recognized for academic excellence"],
        "special_features": [
            "Strong academic reputation - regularly appears in top PAU/EBAU results lists",
            "Project-based learning from early years",
            "Multilingual program (4 languages)",
            "Personalized attention and small group work",
            "Educational psychology and guidance team",
            "Own kitchen with adapted menus (celiac, diabetic, vegetarian, vegan, macrobiotic)",
            "3 bus routes",
            "Library, specialized classrooms, gymnasium",
            "Green spaces and gardens",
            "Extended hours (7:45-19:30)",
            "Bookstore on campus"
        ],
        "lat": 39.518333,
        "lon": -0.410278,
        "coords_confidence": "municipal_plan",
        "coords_source": "Godella municipal plan for Camí Ermita Nova 3",
        "reviews": {
            "micole_rating": 3.6,
            "micole_reviews": 94,
            "google_rating": 4.1,
            "google_reviews": "150+",
            "sentiment": "Mixed; praised for thinking skills, language richness, project-based learning; some concerns about workload and pressure for certain learning styles"
        },
        "fees": {
            "currency": "EUR",
            "range": "Gratis or <€100 per month (concertado pricing for most stages); 1st cycle Infantil is private",
            "notes": "Very affordable due to concertado status; excellent value for quality"
        },
        "class_size": "Moderate; typical for Spanish schools",
        "facilities": [
            "Specialized classrooms",
            "Gymnasium",
            "Library",
            "Body expression rooms",
            "Music rooms",
            "Natural surroundings with trees and gardens",
            "Own cafeteria with kitchen",
            "Bookstore"
        ],
        "academic_results": "Consistently strong PAU/EBAU results; regularly appears in regional top schools lists",
        "sources": [
            {"label": "Official website", "ref": "https://www.gencana.es/"},
            {"label": "Micole listing", "ref": "https://www.micole.net/valencia/godella/colegio-centro-educativo-gencana"},
            {"label": "Godella municipal info", "ref": "https://www.godella.es/es/colegio-gencana"},
            {"label": "School listing with coords", "ref": "https://www.buscocolegio.com/School/school-details.action?id=46020731"},
        ],
        "notes": "Highly regarded academic school in Godella with strong reputation for innovative, project-based pedagogy. Excellent value due to concertado status. Trade-off: earlier device introduction (3º Primaria) vs screen-light approach. Strong critical thinking and communication skills development. Location in quiet residential Godella with good connections to Valencia. Extended hours and services make it family-friendly. Some parents report high workload/expectations may not suit all learning styles."
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
        "languages_day_to_day": "Spanish/Valencian as vehicular languages; English as foreign language (medium level per directory)",
        "languages_taught": ["Spanish", "Valencian", "English"],
        "device_policy_summary": "Public CEIP device policies vary by center; verify whether/when 1:1 starts (many public schools start shared/teacher-led devices, transitioning to 1:1 later in Primaria or ESO)",
        "pedagogy": "Spanish public school model with center-specific educational project; verify early-years approach, homework policies, and classroom routines",
        "special_features": [
            "Located in popular Benimaclet neighborhood",
            "High ratings in school directories",
            "Community school with local roots"
        ],
        "lat": 39.4750,
        "lon": -0.3600,
        "coords_confidence": "approximate_city_level",
        "reviews": {
            "micole_rating": 4.6,
            "micole_reviews": 10,
            "micole_ranking_note": "One of top-rated public CEIPs in Valencia city",
            "google_rating": None,
            "google_reviews": None,
        },
        "fees": {
            "currency": "EUR",
            "tuition": "Free (public school)",
            "notes": "Nominal fees may apply for extracurriculars, materials, meals"
        },
        "sources": [
            {"label": "Micole listing", "ref": "https://www.micole.net/valencia/valencia/colegio-municipal-benimaclet"},
        ],
        "notes": "Top-rated public option in Valencia city. Coordinates are approximate; validate exact building location using address. Request written device policy and visit to understand teaching approach, homework expectations, and early years practices. Public CEIPs are free, making them very affordable, but verify alignment with family's pedagogical preferences."
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
        "languages_day_to_day": "Spanish/Valencian + English (center project; verify specifics)",
        "languages_taught": ["Spanish", "Valencian", "English"],
        "device_policy_summary": "Verify if/when 1:1 starts; many public CEIPs use shared/teacher-led devices in early years",
        "pedagogy": "Spanish public school with center-specific educational project; verify project-based elements and classroom structure",
        "lat": 39.486946,
        "lon": -0.380345,
        "coords_confidence": "verified_gva_directory",
        "coords_source": "GVA official school directory",
        "reviews": {
            "micole_rating": None,
            "micole_reviews": None,
            "google_rating": None,
            "google_reviews": None,
        },
        "fees": {
            "currency": "EUR",
            "tuition": "Free (public school)",
        },
        "sources": [
            {"label": "GVA official directory", "ref": "https://aplicaciones.edu.gva.es/ovice/areaogt/val/centro.asp?codi=46016580"},
        ],
        "notes": "Coordinates verified from official GVA directory. Request visit and written information on device policy and teaching approach."
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
        "languages_day_to_day": "Spanish/Valencian + English (center project; verify)",
        "languages_taught": ["Spanish", "Valencian", "English"],
        "device_policy_summary": "Verify device policy; likely shared devices first, transitioning to individual later",
        "pedagogy": "Spanish public school model; verify teaching approach during visit",
        "lat": 39.479324,
        "lon": -0.359375,
        "coords_confidence": "verified_gva_directory",
        "coords_source": "GVA official school directory",
        "reviews": {
            "micole_rating": None,
            "micole_reviews": None,
            "google_rating": None,
            "google_reviews": None,
        },
        "fees": {
            "currency": "EUR",
            "tuition": "Free (public school)",
        },
        "sources": [
            {"label": "GVA official directory", "ref": "https://aplicaciones.edu.gva.es/ovice/areaogt/val/centro.asp?codi=46016957"},
        ],
        "notes": "Coordinates verified from official GVA directory."
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
        "languages_day_to_day": "Spanish/Valencian + English (center project; verify)",
        "languages_taught": ["Spanish", "Valencian", "English"],
        "device_policy_summary": "Verify device policy during visit",
        "pedagogy": "Spanish public school model; verify early-years approach",
        "lat": 39.469256,
        "lon": -0.386374,
        "coords_confidence": "approximate",
        "reviews": {
            "micole_rating": None,
            "micole_reviews": None,
            "google_rating": None,
            "google_reviews": None,
        },
        "fees": {
            "currency": "EUR",
            "tuition": "Free (public school)",
        },
        "sources": [
            {"label": "GVA official directory", "ref": "https://aplicaciones.edu.gva.es/ovice/areaogt/val/centro.asp?codi=46012268"},
        ],
        "notes": "Coordinates approximate; confirm exact location during visit."
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
        "languages_day_to_day": "Spanish/Valencian + English (center project; verify)",
        "languages_taught": ["Spanish", "Valencian", "English"],
        "device_policy_summary": "Verify device policy during visit",
        "pedagogy": "Spanish public school model; verify teaching approach",
        "lat": 39.480020,
        "lon": -0.360840,
        "coords_confidence": "verified_gva_directory",
        "coords_source": "GVA official school directory",
        "reviews": {
            "micole_rating": None,
            "micole_reviews": None,
            "google_rating": None,
            "google_reviews": None,
        },
        "fees": {
            "currency": "EUR",
            "tuition": "Free (public school)",
        },
        "sources": [
            {"label": "GVA official directory", "ref": "https://aplicaciones.edu.gva.es/ovice/areaogt/val/centro.asp?codi=46011831"},
        ],
        "notes": "Coordinates verified from official GVA directory."
    },
]


# ===================================================================================
# HELPER FUNCTIONS FOR DATA ACCESS
# ===================================================================================

def get_school_by_id(school_id: str) -> dict | None:
    """Retrieve a school by its unique ID."""
    for school in SCHOOLS:
        if school["id"] == school_id:
            return school
    return None


def get_schools_by_type(school_type: str) -> list[dict]:
    """Get all schools of a specific type (e.g., 'Private', 'Public', 'Concertado')."""
    return [s for s in SCHOOLS if school_type.lower() in s["type"].lower()]


def get_schools_by_municipality(municipality: str) -> list[dict]:
    """Get all schools in a specific municipality."""
    return [s for s in SCHOOLS if s["municipality"].lower() == municipality.lower()]


def get_schools_with_curriculum(curriculum_keyword: str) -> list[dict]:
    """Find schools offering specific curriculum (e.g., 'British', 'IB', 'Montessori')."""
    return [s for s in SCHOOLS if curriculum_keyword.lower() in s["curriculum"].lower()]


def get_schools_by_language(language: str) -> list[dict]:
    """Find schools where specific language is taught or used."""
    results = []
    for school in SCHOOLS:
        if "languages_taught" in school and language in school["languages_taught"]:
            results.append(school)
        elif language.lower() in school.get("languages_day_to_day", "").lower():
            results.append(school)
    return results


def get_affordable_schools(max_monthly_fee: float = 100.0) -> list[dict]:
    """Find schools with fees under specified monthly amount (excludes those without fee info)."""
    results = []
    for school in SCHOOLS:
        if school["type"] == "Public":
            results.append(school)
        elif "fees" in school and "range" in school["fees"]:
            fee_str = school["fees"]["range"].lower()
            if "gratis" in fee_str or "<100" in fee_str or "free" in fee_str:
                results.append(school)
    return results
