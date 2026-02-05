# schools_data.py
from typing import Dict, Any, List, Tuple

Source = Tuple[str, str]

SCHOOLS: List[Dict[str, Any]] = [
    # --- Montessori / Alternative ---
    {
        "rank": 1,
        "school": "Imagine Montessori School (Valencia Campus)",
        "type": "Private",
        "address": "C/ Meliana 5, 46019 València, Spain",
        "why": "Montessori + English pathway; Valencia campus serves younger ages (confirm stage coverage for your child).",
        "device_policy": "No published grade-by-grade 1:1 rollout found → request written confirmation.",
        "languages": "EN-led; ES support",
        "academic_proxy": "N/A (non-PAU pathway)",
        "sources": [
            ("ISDB listing (campuses)", "https://www.international-schools-database.com/in/valencia-spain/imagine-montessori-school-valencia"),
            ("IMS bus route PDF (Meliana 5)", "https://imaginemontessori.es/wp-content/uploads/2025/01/Ruta-Escolar-IMS-Summer-Camp-2025-Bus-Route-IMS-Summer-Camp-2025.pdf"),
        ],
        # Optional: set lat/lon manually to avoid geocoding calls
        # "lat": 39.4920, "lon": -0.3560,
    },
    {
        "rank": 2,
        "school": "Imagine Montessori School (La Pinada Campus, Paterna)",
        "type": "Private",
        "address": "Carrer Melissa 46, 46980 Paterna, Valencia, Spain",
        "why": "Montessori + English pathway with longer continuity (often through secondary) — good if you want a single school.",
        "device_policy": "No published grade-by-grade 1:1 rollout found → request written confirmation.",
        "languages": "EN-led; ES support",
        "academic_proxy": "N/A (non-PAU pathway)",
        "sources": [
            ("ISDB listing (campuses)", "https://www.international-schools-database.com/in/valencia-spain/imagine-montessori-school-valencia"),
            ("IMS legal notice (address)", "https://imaginemontessori.es/en/legal-notice-and-terms-of-use/"),
        ],
    },
    {
        "rank": 3,
        "school": "Valencia Montessori School",
        "type": "Private",
        "address": "Published addresses vary: Av. Pío Baroja 3, 46015 Valencia (school site) OR Av. Rei En Jaume 32, 46016 Tavernes Blanques (directory). Confirm current campus.",
        "why": "AMI-style Montessori; strong early-years fit; English-forward model (confirm day-to-day language split).",
        "device_policy": "No public grade-by-grade 1:1 rollout found → request written confirmation.",
        "languages": "EN primary; ES/VAL taught",
        "academic_proxy": "N/A (ends before PAU)",
        "sources": [
            ("School page (Av. Pío Baroja 3)", "https://valenciamontessori.org/our-school/"),
            ("Directory listing (Tavernes Blanques)", "https://www.educateca.com/centros/valencia-montessori.asp"),
            ("Admissions / language model", "https://valenciamontessori.org/admissions/"),
        ],
        # Tip: for geocoding, you may want to replace address with the confirmed single address later.
    },
    {
        "rank": 4,
        "school": "Escuela Internacional Waldorf Valencia",
        "type": "Private / Association",
        "address": "Camino Cebolla 5, 46540 El Puig de Santa Maria, Valencia, Spain",
        "why": "Explicit ‘no screens in childhood’ stance; strong pedagogy match; confirm progression through Primary for your timeline.",
        "device_policy": "School states tech access begins from Secundaria (explicit on site).",
        "languages": "ES-led (+ EN; verify intensity)",
        "academic_proxy": "N/A",
        "sources": [
            ("Why Waldorf (no screens + tech from Secundaria)", "https://escuelawaldorfvalencia.com/por-que-elegir-una-escuela-waldorf/"),
            ("Contact (address)", "https://escuelawaldorfvalencia.com/contacto/"),
        ],
    },

    # --- English pathway ---
    {
        "rank": 5,
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
        "rank": 6,
        "school": "British School of Valencia (BSV)",
        "type": "Private",
        "address": "C/ Filipinas 37, 46006 València, Spain",
        "why": "In-city British option; strong pathway but weaker screen fit vs your red line.",
        "device_policy": "School states a 1:1 programme from Year 3 to Year 13 (published).",
        "languages": "EN-led + ES",
        "academic_proxy": "N/A (British exams)",
        "sources": [
            ("Digital Learning Programme", "https://www.bsvalencia.com/digital-learning-programme/"),
            ("Campus info", "https://www.bsvalencia.com/es/campus-bsv-nexus/"),
        ],
    },
    {
        "rank": 7,
        "school": "English School Los Olivos",
        "type": "Private",
        "address": "Campo Olivar, 46110 Godella, Valencia, Spain",
        "why": "English pathway + German offered; screen stance must be verified carefully.",
        "device_policy": "No public grade-by-grade 1:1 rollout found → request written confirmation.",
        "languages": "EN-led + ES + DE",
        "academic_proxy": "N/A (British exams)",
        "sources": [
            ("Contact (addresses)", "https://www.los-olivos.es/contacto/"),
            ("Admissions/fees", "https://www.los-olivos.es/admisiones/"),
        ],
    },

    # --- German pathway ---
    {
        "rank": 8,
        "school": "Deutsche Schule Valencia / Colegio Alemán",
        "type": "Private",
        "address": "C/ Jaume Roig 14–16, 46010 València, Spain",
        "why": "Best Spanish–German pathway; academics strong; confirm entry route for age 5.",
        "device_policy": "Tablets reported at 5º (school post) → confirm full rollout in writing.",
        "languages": "DE + ES (+ EN)",
        "academic_proxy": "PAU not primary proxy (German/Spanish pathways vary)",
        "sources": [
            ("Contact (address)", "https://dsvalencia.org/es/contacto/"),
            ("Tablet post (evidence)", "https://www.facebook.com/deutscheschulevalencia/posts/nuestros-nuevos-alumnos-de-5-curso-entran-en-la-era-digital-como-parte-de-nuestr/802012752121027/"),
        ],
    },

    # --- Spanish mainstream / strong reputation ---
    {
        "rank": 9,
        "school": "Centro Educativo Gençana",
        "type": "Private / Concertado mix",
        "address": "C/ Ermita Nova 3, 46110 Godella, Valencia, Spain",
        "why": "Strong reputation; trade-off on earlier 1:1 devices.",
        "device_policy": "Press profile reports Chromebook from 3º Primaria → verify latest in writing.",
        "languages": "ES/VAL + EN",
        "academic_proxy": "Reputation proxy; appears in ‘top results’ lists (verify year)",
        "sources": [
            ("El Mundo special PDF (device statement)", "https://fuenllana.net/wp-content/uploads/2024/03/240306-El-Mundo-Especial-colegios-Los-cien-ma%CC%81s-notables.pdf"),
            ("School site (address)", "https://www.gencana.es/"),
        ],
    },

    # --- Public CEIPs (top-rated list proxy) ---
    {
        "rank": 10,
        "school": "CEIP Municipal Benimaclet",
        "type": "Public",
        "address": "C/ de l'Arquitecte Arnau s/n, València, Spain",
        "why": "Top-rated public CEIP in Valencia city (directory proxy).",
        "device_policy": "Not published → ask school for written policy (1:1 + homework platforms).",
        "languages": "ES / VAL",
        "academic_proxy": "MiCole top-rated public CEIP list",
        "sources": [
            ("MiCole list (public Valencia city)", "https://www.micole.net/valencia/mejores-colegios-publicos-de-valencia"),
        ],
    },
    {
        "rank": 11,
        "school": "CEIP Francisco Giner de los Ríos",
        "type": "Public",
        "address": "Plaça Grup Parpalló, València, Spain",
        "why": "Strong public reputation; good community fit (directory proxy).",
        "device_policy": "Not published → ask school for written policy.",
        "languages": "ES / VAL",
        "academic_proxy": "MiCole top-rated public CEIP list",
        "sources": [
            ("MiCole list (public Valencia city)", "https://www.micole.net/valencia/mejores-colegios-publicos-de-valencia"),
        ],
    },
    {
        "rank": 12,
        "school": "CEIP Rodríguez Fornos",
        "type": "Public",
        "address": "C/ de la Mare de Déu de la Cabeza 26, València, Spain",
        "why": "Consistently well-rated public option (directory proxy).",
        "device_policy": "Not published → ask school for written policy.",
        "languages": "ES / VAL",
        "academic_proxy": "MiCole top-rated public CEIP list",
        "sources": [
            ("MiCole list (public Valencia city)", "https://www.micole.net/valencia/mejores-colegios-publicos-de-valencia"),
        ],
    },
    {
        "rank": 13,
        "school": "CEIP Jaime Balmes",
        "type": "Public",
        "address": "C/ del Mestre Aguilar 15, València, Spain",
        "why": "High-demand public CEIP (directory proxy).",
        "device_policy": "Not published → ask school for written policy.",
        "languages": "ES / VAL",
        "academic_proxy": "MiCole top-rated public CEIP list",
        "sources": [
            ("MiCole list (public Valencia city)", "https://www.micole.net/valencia/mejores-colegios-publicos-de-valencia"),
        ],
    },
    {
        "rank": 14,
        "school": "CEIP IVAF–Luis Fortich",
        "type": "Public",
        "address": "C/ Juan de Garay 23, València, Spain",
        "why": "Strong inclusion + reputation (directory proxy).",
        "device_policy": "Not published → ask school for written policy.",
        "languages": "ES / VAL",
        "academic_proxy": "MiCole top-rated public CEIP list",
        "sources": [
            ("MiCole list (public Valencia city)", "https://www.micole.net/valencia/mejores-colegios-publicos-de-valencia"),
        ],
    },
]
