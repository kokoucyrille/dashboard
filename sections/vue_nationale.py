import streamlit as st

from components.charts import bar_chart, empty_state, insight, line_chart, section_title
from components.kpi import render_kpi_row
from utils.data_loader import has_columns
from utils.formatting import compute_delta_pct, format_number


def render(df, filters):
    section_title("Vue nationale de l'économie numérique", "Où en est l'économie numérique du Togo ?")

    kpis = _build_kpis(df)
    render_kpi_row(kpis)

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Évolution des indicateurs clés", "Comment évolue l'économie numérique dans le temps ?")
        if has_columns(df, ["annee", "valeur", "indicateur"]):
            fig = line_chart(df, x="annee", y="valeur", color="indicateur")
            st.plotly_chart(fig, width="stretch")
            insight(_trend_insight(df))
        else:
            empty_state(
                "Évolution temporelle",
                "Attendu : colonnes `annee`, `indicateur`, `valeur` dans dataset_economie_numerique.csv.",
            )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Classement des régions", "Quelles régions sont les plus avancées numériquement ?")
        if has_columns(df, ["region", "score_deficit_numerique"]):
            agg = df.groupby("region", as_index=False)["score_deficit_numerique"].mean()
            fig = bar_chart(agg, x="region", y="score_deficit_numerique")
            st.plotly_chart(fig, width="stretch")
        else:
            empty_state(
                "Comparaison régionale",
                "Attendu : colonnes `region`, `score_deficit_numerique`.",
            )
        st.markdown("</div>", unsafe_allow_html=True)


def _build_kpis(df):
    if not has_columns(df, ["indicateur", "valeur"]):
        return [
            {"icon": "🧑🏽‍🤝‍🧑🏽", "label": "Population numérique", "value": None},
            {"icon": "📶", "label": "Pénétration Internet", "value": None},
            {"icon": "🏢", "label": "Entreprises numériques", "value": None},
            {"icon": "💼", "label": "Emplois numériques", "value": None},
        ]
    # Une fois les données chargées, ces agrégations deviennent réelles.
    return [
        {"icon": "🧑🏽‍🤝‍🧑🏽", "label": "Population numérique", "value": format_number(df["valeur"].sum())},
        {"icon": "📶", "label": "Pénétration Internet", "value": format_number(df["valeur"].mean(), decimals=1, suffix=" %")},
        {"icon": "🏢", "label": "Entreprises numériques", "value": format_number(df["valeur"].count())},
        {"icon": "💼", "label": "Emplois numériques", "value": None},
    ]


def _trend_insight(df):
    """Génère un court commentaire à partir des données réelles (aucune valeur inventée)."""
    try:
        by_year = df.groupby("annee")["valeur"].mean()
        delta = compute_delta_pct(by_year.iloc[-1], by_year.iloc[0])
        if delta is None:
            return "Tendance en cours d'analyse."
        direction = "progressé" if delta >= 0 else "reculé"
        return f"L'indicateur moyen a {direction} de {abs(delta):.1f} % sur la période observée."
    except Exception:
        return "Tendance en cours d'analyse."
