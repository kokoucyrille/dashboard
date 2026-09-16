import base64
from pathlib import Path

import streamlit as st

CSS_PATH = Path(__file__).resolve().parent.parent / "styles" / "custom.css"
ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"


def inject_css():
    """Injecte la police Inter (Google Fonts) et la feuille de style du projet."""
    st.markdown(
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" '
        'rel="stylesheet">',
        unsafe_allow_html=True,
    )
    if CSS_PATH.exists():
        with open(CSS_PATH, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


_LOGO_MIME = {
    ".svg": "image/svg+xml",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
}


def find_ministry_logo() -> Path | None:
    """
    Cherche un logo du ministère déposé dans assets/ (voir assets/README.md).
    Ordre de priorité : logo_ministere.svg > .png > .jpg > .jpeg > .webp.
    Retourne None si aucun fichier réel n'a été fourni — le header affiche
    alors un badge neutre plutôt qu'un logo inventé.
    """
    for ext in (".svg", ".png", ".jpg", ".jpeg", ".webp"):
        candidate = ASSETS_DIR / f"logo_ministere{ext}"
        if candidate.exists():
            return candidate
    return None


def logo_data_uri() -> str | None:
    """Encode le logo trouvé (si présent) en data URI base64 pour l'injecter dans le HTML du header."""
    path = find_ministry_logo()
    if path is None:
        return None
    mime = _LOGO_MIME.get(path.suffix.lower(), "image/png")
    data = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{data}"
