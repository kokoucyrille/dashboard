import streamlit as st

from components.charts import bar_chart, donut_chart, empty_state, section_title
from utils.data_loader import has_columns


def render(df, filters):
    section_title("Entreprises numériques", "Quels acteurs et quels secteurs contribuent le plus à l'économie numérique ?")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Classement des secteurs", "Quels secteurs contribuent le plus ?")
        if has_columns(df, ["secteur", "nombre_entreprises"]):
            agg = df.groupby("secteur", as_index=False)["nombre_entreprises"].sum()
            agg = agg.sort_values("nombre_entreprises", ascending=False)
            st.plotly_chart(bar_chart(agg, x="secteur", y="nombre_entreprises"), width="stretch")
        else:
            empty_state("Classement des secteurs", "Attendu : colonnes `secteur`, `nombre_entreprises`.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Répartition par type d'opérateur", "")
        if has_columns(df, ["type_operateur", "nombre_entreprises"]):
            st.plotly_chart(
                donut_chart(df, names="type_operateur", values="nombre_entreprises"),
                width="stretch",
            )
        else:
            empty_state(
                "Répartition par opérateur",
                "Attendu : colonnes `type_operateur` (ex. Moov, Togocom, Mobile Money, Data Center), `nombre_entreprises`.",
            )
        st.markdown("</div>", unsafe_allow_html=True)
