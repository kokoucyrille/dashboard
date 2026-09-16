"""
TOGO DIGITAL INTELLIGENCE
Plateforme d'intelligence territoriale pour le pilotage de l'économie
numérique du Togo.

Ce fichier est le point d'entrée unique de l'application (pas de dossier
`pages/` Streamlit natif, pour garder la navigation horizontale personnalisée
et éviter la sidebar comme menu principal — voir components/navigation.py).
"""
import streamlit as st

from components.filters import render_filters
from components.footer import render_footer
from components.header import render_header
from components.navigation import SECTIONS, render_navigation
from sections import (
    accueil,
    ecosysteme_numerique,
    indicateurs,
    infrastructures,
    territoires,
    vue_nationale,
)
from utils.data_loader import load_csv
from utils.style_helpers import inject_css

st.set_page_config(
    page_title="TOGO DIGITAL INTELLIGENCE",
    page_icon="🇹🇬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_css()
render_header()

if "active_section" not in st.session_state:
    st.session_state.active_section = "Accueil"

selected = render_navigation(default_index=SECTIONS.index(st.session_state.active_section))
st.session_state.active_section = selected

# Dataset principal — renomme le fichier ici une fois les exports du notebook
# déposés dans data/ (voir data/README.md pour le schéma attendu).
df = load_csv("dataset_economie_numerique.csv")

# 6 entrées maximum dans le menu horizontal (voir components/navigation.py) :
# Entreprises + Usages numériques ont été fusionnées en "Écosystème numérique".
SECTIONS_WITH_FILTERS = {
    "Vue nationale": vue_nationale,
    "Territoires": territoires,
    "Infrastructures": infrastructures,
    "Écosystème numérique": ecosysteme_numerique,
    "Indicateurs": indicateurs,
}
SECTIONS_WITHOUT_FILTERS = {
    "Accueil": accueil,
}

st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

if selected in SECTIONS_WITH_FILTERS:
    col_filters, col_content = st.columns([1, 4], gap="large")
    with col_filters:
        st.markdown('<div class="tdi-filters-card">', unsafe_allow_html=True)
        filters = render_filters(df)
        st.markdown("</div>", unsafe_allow_html=True)
    with col_content:
        SECTIONS_WITH_FILTERS[selected].render(df, filters)
else:
    SECTIONS_WITHOUT_FILTERS[selected].render(df)

render_footer()
