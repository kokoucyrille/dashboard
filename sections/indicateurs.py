import streamlit as st

from components.charts import empty_state, gauge, heatmap, section_title
from utils.data_loader import has_columns
from utils.formatting import format_number


def render(df, filters):
    section_title("Indicateurs & priorités", "Quels territoires nécessitent une intervention prioritaire ?")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Score de déficit numérique national", "")
        if has_columns(df, ["score_deficit_numerique"]):
            st.plotly_chart(gauge(df["score_deficit_numerique"].mean(), title="Score moyen"), width="stretch")
        else:
            empty_state("Score national", "Attendu : colonne `score_deficit_numerique`.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Préfectures × indicateurs", "Où se cumulent les faiblesses ?")
        if has_columns(df, ["prefecture", "indicateur", "valeur"]):
            st.plotly_chart(heatmap(df, x="indicateur", y="prefecture", z="valeur"), width="stretch")
        else:
            empty_state("Heatmap des indicateurs", "Attendu : colonnes `prefecture`, `indicateur`, `valeur`.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
    section_title("Table des zones prioritaires", "")
    if has_columns(df, ["prefecture", "score_deficit_numerique"]):
        table = (
            df.groupby("prefecture", as_index=False)["score_deficit_numerique"]
            .mean()
            .sort_values("score_deficit_numerique", ascending=False)
        )
        table["score_deficit_numerique"] = table["score_deficit_numerique"].map(lambda v: format_number(v, decimals=1))
        st.dataframe(table, width="stretch", hide_index=True, height=340)
    else:
        empty_state(
            "Table des zones prioritaires",
            "Attendu : colonnes `prefecture`, `score_deficit_numerique` (produit par le notebook d'analyse).",
        )
    st.markdown("</div>", unsafe_allow_html=True)
