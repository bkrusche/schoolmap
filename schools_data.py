# schools_data.py
from typing import Dict, Any, List, Tuple, Optional

Source = Tuple[str, str]

SCHOOLS: List[Dict[str, Any]] = [
    # ----------------------------
    # Montessori / alternative
    # ----------------------------
    {
        "rank": 1,
        "school": "Imagine Montessori School",
        "campus": "Valencia Campus (Ages ~2–9)",
        "type": "Private",
        "address": "C/ Meliana 5, 46019 València, Spain",
        "why": "Montessori + English pathway; city campus for early years.",
        "device_policy": "No published grade-by-grade 1:1 rollout found → request written confirmation.",
        "languages": "EN-led; ES support",
        "academic_proxy": "N/A (non-PAU pathway)",
        "sources": [
            ("International Schools Database (both campuses + addresses)", "https://www.international-schools-database.com/in/valencia-spain/imagine-montessori-school-valencia"),
            ("LinkedIn locations (Meliana 5 + Melissa 46)", "https://es.linkedin.com/company/imagine-montessori-school"),
        ],
    },
    {
        "rank": 2,
        "school": "Imagine Montessori School",
        "campus": "La Pinada Campus, Paterna (Ages ~2–18)",
        "type": "Private",
        "address": "Carrer Melissa 46, 46980 Paterna, Valencia, Spain",
        "why": "Longer continuity through later stages (confirm exact stage availability for your child).",
        "device_policy": "No published grade-by-grade 1:1 rollout found → request written confirmation.",
        "languages": "EN-led; ES support",
        "academic_proxy": "N/A (non-PAU pathway)",
        "sources": [
            ("International Schools Database (both campuses + addresses)", "https://www.international-schools-database.com/in/valencia-spain/imagine-montessori-school-valencia"),
            ("Legal notice (Melissa 46, Paterna)", "https://imaginemontessori.es/en/legal-notice-and-terms-of-use/"),
        ],
    },
    {
        "rank": 3,
        "school": "Valencia Montessori School",
        "campus": "Main campus (confirm on visit)",
        "type": "Private",
        "address": "Avinguda del Rei en Jaume 32, 46016 Tavernes Blanques, Valencia, Spain",
        "why": "AMI-oriented Montessori; strong early-years fit; verify day-to-day language model.",
        "device_policy": "No public grade-by-grade 1:1 rollout found → request written confirmation.",
        "languages": "EN-forward + ES/VAL (verify split by stage)",
        "academic_proxy": "N/A (Primary-only)",
        "other_addresses": [
            "Office / published contact on site: Av. Pío Baroja 3, 46015 Valencia, Spain"
        ],
        "sources": [
            ("Educateca listing (Rei En Jaume 32, Tavernes Blanques)", "https://www.educateca.com/centros/valencia-montessori.asp"),
            ("Facebook ‘About’ (Rei en Jaume 32)", "https://es-la.facebook.com/valenciamontessori/about/"),
            ("VMS admissions/contact block (Pío Baroja 3 listed)", "https://valenciamontessori.org/admissions/"),
        ],
    },
    {
        "rank": 4,
        "school": "Escuela Internacional Waldorf Valencia",
        "campus": "El Puig",
        "type": "Private / Association",
        "address": "Camino Cebolla 5, 46540 El Puig de Santa Maria, Valencia, Spain",
        "why": "Explicit ‘no screens in childhood’ stance; strong pedagogy match.",
        "device_policy": "School states tech access begins from Secundaria (published stance).",
        "languages": "ES-led (+ EN; verify intensity)",
        "academic_proxy": "N/A",
        "sources": [
            ("Contact (address)", "https://escuelawaldorfvalencia.com/contacto/"),
            ("Why Waldorf (screens/tech stance)", "https://escuelawaldorfvalencia.com/por-que-elegir-una-escuela-waldorf/"),
        ],
    },

    # ----------------------------
    # English international pathway
    # ----------------------------
    {
        "rank": 5,
        "school": "British College La Cañada",
        "campus": "La Cañada (Paterna)",
        "type": "Private",
        "address": "Calle 232 Nº 110, 46182 La Cañada (Paterna), Valencia, Spain",
        "why": "Mainstream option with unusually clear tech policy.",
        "device_policy": "School states BYOD implemented from KS4 to Sixth Form (published).",
        "languages": "EN-led + ES",
        "academic_proxy": "N/A (British exams)",
        "sources": [
            ("Contact / location (address)", "https://www.britishcollegelacanyada.es/en/contact/"),
            ("Digital learning policy", "https://www.britishcollegelacanyada.es/en/educational-project/digital-learning/"),
        ],
    },
    {
        "rank": 6,
        "school": "British School of Valencia (BSV)",
        "campus": "Main Campus (Early Years–Secondary)",
        "type": "Private",
        "address": "Calle Filipinas 37, 46006 Valencia, Spain",
        "why": "In-city British option; strong pathway but weaker screen fit vs your red line.",
        "device_policy": "School states a 1:1 programme from Year 3 to Year 13 (published).",
        "languages": "EN-led + ES",
        "academic_proxy": "N/A (British exams)",
        "sources": [
            ("Contact Us (Filipinas 37)", "https://www.bsvalencia.com/contact-us/"),
            ("Digital learning programme", "https://www.bsvalencia.com/digital-learning-programme/"),
        ],
    },
    {
        "rank": 7,
        "school": "English School Los Olivos",
        "campus": "Primary site",
        "type": "Private",
        "address": "C/ Pino Panera 25, 46110 Campo Olivar-Godella, Valencia, Spain",
        "why": "English pathway; German offered; verify screen policy carefully.",
        "device_policy": "No public grade-by-grade 1:1 rollout found → request written confirmation.",
        "languages": "EN-led + ES + DE",
        "academic_proxy": "N/A (British exams)",
        "other_addresses": [
            "Secondary site: Av. de los Almendros 13, 46110 Campo Olivar-Godella, Valencia"
        ],
        "sources": [
            ("Los Olivos contact page (Primary + Secondary addresses)", "https://www.los-olivos.es/contacto/"),
        ],
    },

    # ----------------------------
    # German pathway
    # ----------------------------
    {
        "rank": 8,
        "school": "Deutsche Schule Valencia / Colegio Alemán",
        "campus": "Valencia",
        "type": "Private",
        "address": "C/ Jaume Roig 14–16, 46010 Valencia, Spain",
        "why": "Best Spanish–German pathway; confirm entry route for age 5 and device rollout by grade.",
        "device_policy": "Tablets reported at 5º (school post) → confirm full rollout in writing.",
        "languages": "DE + ES (+ EN)",
        "academic_proxy": "Not PAU-centric (German pathway varies)",
        "sources": [
            ("Official contact page (address)", "https://dsvalencia.org/es/contacto/"),
        ],
    },

    # ----------------------------
    # Spanish mainstream / strong reputation
    # ----------------------------
    {
        "rank": 9,
        "school": "Centro Educativo Gençana",
        "campus": "Godella",
        "type": "Private / Concertado mix",
        "address": "C/ Ermita Nova 3, 46110 Godella, Valencia, Spain",
        "why": "Strong reputation; trade-off on earlier 1:1 devices (verify current year).",
        "device_policy": "Press profile reports Chromebook from 3º Primaria → verify latest in writing.",
        "languages": "ES/VAL + EN",
        "academic_proxy": "Reputation proxy (verify year-specific outcomes if needed)",
        "sources": [
            ("School localisation page (address)", "https://www.gencana.es/localizacion/"),
            ("GVA guide of centres (address)", "https://aplicaciones.edu.gva.es/ocd/areacd/es/centro.asp?Codi=46020731"),
        ],
    },

    # ----------------------------
    # Public CEIPs (València city)
    # ----------------------------
    {
        "rank": 10,
        "school": "CEIP Municipal Benimaclet",
        "campus": "València",
        "type": "Public",
        "address": "Carrer de l'Arquitecte Arnau s/n, 46020 Valencia, Spain",
        "why": "Highly rated public CEIP (directory proxy) — confirm classroom approach and device policy.",
        "device_policy": "Not published → ask school for written policy (1:1 + homework platforms).",
        "languages": "ES / VAL",
        "academic_proxy": "Directory rating proxy (MiCole)",
        "sources": [
            ("MiCole school page (address)", "https://www.micole.net/valencia/valencia/colegio-municipal-benimaclet"),
        ],
    },
    {
        "rank": 11,
        "school": "CEIP Francisco Giner de los Ríos (València)",
        "campus": "València",
        "type": "Public",
        "address": "Plaça Grup Parpalló s/n, 46015 València, Spain",
        "why": "Strong public reputation proxy; verify language line + device policy.",
        "device_policy": "Not published → ask school for written policy.",
        "languages": "ES / VAL (+ EN as subject)",
        "academic_proxy": "Public school proxy (verify locally)",
        "sources": [
            ("Official school portal contact (address)", "https://portal.edu.gva.es/ginerdelosrios/contacto-y-localizacion/"),
        ],
    },
    {
        "rank": 12,
        "school": "CEIP Rodríguez Fornos",
        "campus": "València",
        "type": "Public",
        "address": "Carrer de la Mare de Déu de la Cabeza 26, 46014 València, Spain",
        "why": "Well-rated public CEIP; confirm pedagogy + device policy.",
        "device_policy": "Not published → ask school for written policy.",
        "languages": "ES / VAL (+ EN as subject)",
        "academic_proxy": "Directory rating proxy (MiCole)",
        "sources": [
            ("MiCole school page (address)", "https://www.micole.net/valencia/valencia/colegio-rodriguez-fornos"),
            ("Official school portal (address)", "https://portal.edu.gva.es/ceiprodriguezfornos/"),
        ],
    },
    {
        "rank": 13,
        "school": "CEIP Jaime Balmes",
        "campus": "València",
        "type": "Public",
        "address": "C/ Maestro Aguilar 15, 46006 València, Spain",
        "why": "High-demand public CEIP; confirm pedagogy + device policy.",
        "device_policy": "Not published → ask school for written policy.",
        "languages": "ES / VAL (+ EN as subject)",
        "academic_proxy": "Directory rating proxy (MiCole)",
        "sources": [
            ("GVA department listing (address)", "https://www.gva.es/es/inicio/atencion_ciudadano/buscadores/departamentos/detalle_departamentos?id_dept=22483"),
            ("MiCole school page (address)", "https://www.micole.net/valencia/valencia/colegio-jaime-balmes"),
        ],
    },
    {
        "rank": 14,
        "school": "CEIP IVAF–Luis Fortich",
        "campus": "València",
        "type": "Public",
        "address": "C/ Juan de Garay 23, 46017 València, Spain",
        "why": "Strong inclusion profile; confirm pedagogy + device policy.",
        "device_policy": "Not published → ask school for written policy.",
        "languages": "ES / VAL (+ EN as subject)",
        "academic_proxy": "Official listing proxy",
        "sources": [
            ("GVA Guide of Centres (address)", "https://aplicaciones.edu.gva.es/ocd/areacd/es/centro.asp?codi=46011831"),
            ("MiCole school page (address)", "https://www.micole.net/valencia/valencia/colegio-ivaf-luis-fortich"),
        ],
    },
]
