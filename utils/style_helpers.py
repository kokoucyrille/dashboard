from pathlib import Path

import streamlit as st

CSS_PATH = Path(__file__).resolve().parent.parent / "styles" / "custom.css"


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
