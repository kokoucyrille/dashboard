import streamlit as st

from components.kpi import render_kpi_row
from utils.data_loader import has_columns
from utils.formatting import format_number

CARDS = [
    ("📊", "Vue nationale", "Indicateurs clés et évolution", "Vue nationale"),
    ("📍", "Territoires", "Régions et préfectures", "Territoires"),
    ("🗼", "Infrastructures", "Agences, Mobile Money, data centers", "Infrastructures"),
    ("🏢", "Écosystème numérique", "Entreprises, secteurs et usages", "Écosystème numérique"),
    ("🧭", "Indicateurs", "Score de déficit et priorités", "Indicateurs"),
]


def render(df):
    st.markdown(
        """
        <div class="tdi-hero">
            <h1>Piloter l'économie numérique du <span class="tdi-hero-accent">Togo</span></h1>
            <p>Connectivité, infrastructures et usages — en un coup d'œil.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    kpis = [
        {"icon": "🧑🏽‍🤝‍🧑🏽", "label": "Population numérique", "value": _safe_count(df, "population_numerique")},
        {"icon": "📶", "label": "Taux de pénétration Internet", "value": _safe_pct(df, "penetration_internet")},
        {"icon": "🏢", "label": "Entreprises numériques", "value": _safe_count(df, "entreprises_numeriques")},
        {"icon": "💼", "label": "Emplois numériques", "value": _safe_count(df, "emplois_numeriques")},
    ]
    render_kpi_row(kpis)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    cols = st.columns(len(CARDS))
    for i, (icon, title, text, target) in enumerate(CARDS):
        with cols[i]:
            st.markdown(
                f"""
                <div class="tdi-nav-card">
                    <div class="tdi-nav-card-icon">{icon}</div>
                    <div class="tdi-nav-card-title">{title}</div>
                    <div class="tdi-nav-card-text">{text}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Ouvrir →", key=f"home_nav_{target}", width="stretch"):
                st.session_state.active_section = target
                st.rerun()


def _safe_count(df, column):
    if has_columns(df, [column]):
        return format_number(df[column].sum())
    return None


def _safe_pct(df, column):
    if has_columns(df, [column]):
        return format_number(df[column].mean(), decimals=1, suffix=" %")
    return None
