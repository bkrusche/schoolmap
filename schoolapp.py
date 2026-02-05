"""
schools_data.py
Valencia-area schools dataset for the Streamlit map app.

Notes:
- lat/lon are included to avoid runtime geocoding.
- Some coordinates are approximations when a primary source with exact coordinates was not accessible.
  These rows are clearly flagged with `coords_confidence="approx"` and should be validated quickly in Google Maps.
"""

from __future__ import annotations

SCHOOLS = [
    # --- Screen-light / alternative pedagogy / Montessori ---
    {
        "id": "imagine_montessori_valencia",
        "name": "Imagine Montessori School (Valencia campus)",
        "type": "Private",
        "address": "Calle Meliana, 5, 46019 València, Valencia, Spain",
        "municipality": "València",
        "stages": "Infantil (20m–6), Primaria (6–12), Secundaria/Pre-U (12–18) via wider school; Valencia campus reported 2–9",
        "curriculum": "British + Montessori (accepted by Spanish Ministry of Education)",
        "languages_day_to_day": "English-led; Spanish/Valencian introduced from Primaria (per directories/official site).",
        "device_policy_summary": "Montessori approach typically screen-light in early years; confirm exact 1:1 timing by stage/campus during visit.",
        "pedagogy": "Montessori",
        "lat": 39.470239,
        "lon": -0.376805,
        "coords_confidence": "approx_street_centroid",
        "reviews": {
            "micole_rating": None,
            "micole_reviews": None,
            "google_rating": None,
            "google_reviews": None,
        },
        "sources": [
            {"label": "Official site (programmes / Montessori + British)", "ref": "https://imaginemontessori.es/"},
            {"label": "Official legal notice (Paterna campus address)", "ref": "https://imaginemontessori.es/aviso-legal/"},
            {"label": "International Schools Database (two-campus addresses)", "ref": "https://www.international-schools-database.com/in/valencia-spain/imagine-montessori-school-valencia"},
            {"label": "Address reference (Calle Meliana 5)", "ref": "https://startupxplore.com/en/startups/imagine-montessori-school"},
            {"label": "Street coordinate (calle centroid; validate building # in Maps)", "ref": "https://www.codigospostal.org/calles/4/cp.php?MELIANA=&id=8916"},
        ],
        "notes": "The coordinate source provides a street-level lat/lon; verify the pin matches the exact entrance."
    },
    {
        "id": "gencana",
        "name": "Centro Educativo Gençana",
        "type": "Concertado/Private",
        "address": "Camí Ermita Nova, 3, 46110 Godella, Valencia, Spain",
        "municipality": "Godella",
        "stages": "Infantil, Primaria, ESO, Bachillerato",
        "curriculum": "Spanish (LOMLOE) + bilingual programmes (school-defined)",
        "languages_day_to_day": "Spanish/Valencian + English (school-defined bilingual model; verify immersion by stage).",
        "device_policy_summary": "Reported Chromebook 1:1 from 3º Primaria (verify current policy with school handbook).",
        "pedagogy": "Project-based / competency-based (school-defined); verify classroom routines in Infantil/Primaria.",
        "lat": 39.518333,
        "lon": -0.410278,
        "coords_confidence": "municipal_plan_coords",
        "reviews": {"micole_rating": None, "micole_reviews": None, "google_rating": None, "google_reviews": None},
        "sources": [
            {"label": "School profile (MiCole)", "ref": "https://www.micole.net/valencia/godella/colegio-gencana"},
            {"label": "Godella municipal plan (includes coords for Camí Ermita Nova 3)", "ref": "https://godella.es/wp-content/uploads/2020/11/PAM_GODELLA_2020_2023.pdf"},
            {"label": "GVA private/concerted centres registry (basic listing)", "ref": "https://registre.ods.gva.es/centre/export?format=ods&dist=E&dist02=E0&export_all=True&lang=es"},
        ],
        "notes": "Coords derived from municipal plan for the address; confirm against Google Maps pin."
    },

    # --- German pathway ---
    {
        "id": "deutsche_schule_valencia",
        "name": "Colegio Alemán de Valencia (Deutsche Schule Valencia)",
        "type": "Private",
        "address": "C/ Jaume Roig, 14–16, 46010 València, Valencia, Spain",
        "municipality": "València",
        "stages": "Kindergarten/Infantil, Primaria, Sek I/ESO equivalent, Sek II (Abitur pathway varies by cohort)",
        "curriculum": "German curriculum + Spanish homologation (verify exact leaving qualifications offered)",
        "languages_day_to_day": "German-led with Spanish; English often added (verify split by stage).",
        "device_policy_summary": "Reported tablets issued around 5º Primaria+ (verify current 1:1 start and device type).",
        "pedagogy": "German school pedagogy; verify early-years approach and play-based learning in Kindergarten.",
        "lat": 39.4772437,
        "lon": -0.3594103,
        "coords_confidence": "map_source",
        "reviews": {"micole_rating": None, "micole_reviews": None, "google_rating": None, "google_reviews": None},
        "sources": [
            {"label": "Map-based coordinates (Maptons listing)", "ref": "https://maptons.com/pe/c/valencia-2043630208/"},
        ],
        "notes": "Coordinates sourced from a map listing; validate against school's official contact page when you visit."
    },
