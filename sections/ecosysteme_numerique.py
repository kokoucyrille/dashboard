import streamlit as st

from components.charts import (
    bar_chart,
    donut_chart,
    empty_state,
    insight,
    line_chart,
    scatter_chart,
    section_title,
)
from utils.data_loader import has_columns
from utils.formatting import compute_delta_pct

# Fusion des anciennes sections "Entreprises" + "Usages numeriques" :
# qui produit l'ecosysteme numerique, et comment les usages en decoulent.
# 4 graphiques en grille 2x2 - zero paragraphe, uniquement des titres
# et des questions courtes.


def render(df, filters):
    section_title("Écosystème numérique", "Acteurs, secteurs et usages de l'économie numérique")

    row1_col1, row1_col2 = st.columns([3, 2])

    with row1_col1:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Secteurs les plus contributeurs", "")
        if has_columns(df, ["secteur", "nombre_entreprises"]):
            agg = df.groupby("secteur", as_index=False)["nombre_entreprises"].sum()
            agg = agg.sort_values("nombre_entreprises", ascending=False)
            st.plotly_chart(bar_chart(agg, x="secteur", y="nombre_entreprises"), width="stretch")
        else:
            empty_state("Classement des secteurs", "Attendu : colonnes `secteur`, `nombre_entreprises`.")
        st.markdown("</div>", unsafe_allow_html=True)

    with row1_col2:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Répartition par opérateur", "")
        if has_columns(df, ["type_operateur", "nombre_entreprises"]):
            st.plotly_chart(
                donut_chart(df, names="type_operateur", values="nombre_entreprises"),
                width="stretch",
            )
        else:
            empty_state(
                "Répartition par opérateur",
                "Attendu : colonnes `type_operateur`, `nombre_entreprises`.",
            )
        st.markdown("</div>", unsafe_allow_html=True)

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Évolution des usages numériques", "")
        if has_columns(df, ["annee", "taux_usage_numerique"]):
            agg = df.groupby("annee", as_index=False)["taux_usage_numerique"].mean()
            st.plotly_chart(line_chart(agg, x="annee", y="taux_usage_numerique"), width="stretch")
            delta = compute_delta_pct(
                agg["taux_usage_numerique"].iloc[-1], agg["taux_usage_numerique"].iloc[0]
            )
            if delta is not None:
                direction = "accéléré" if delta >= 0 else "ralenti"
                insight(f"Usage {direction} de {abs(delta):.1f} % sur la période.")
        else:
            empty_state("Évolution des usages", "Attendu : colonnes `annee`, `taux_usage_numerique`.")
        st.markdown("</div>", unsafe_allow_html=True)

    with row2_col2:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Infrastructures vs usages", "")
        if has_columns(df, ["nb_agents_mobile_money", "taux_usage_numerique"]):
            st.plotly_chart(
                scatter_chart(
                    df,
                    x="nb_agents_mobile_money",
                    y="taux_usage_numerique",
                    color="region" if "region" in df.columns else None,
                ),
                width="stretch",
            )
        else:
            empty_state(
                "Infrastructures / usages",
                "Attendu : colonnes `nb_agents_mobile_money`, `taux_usage_numerique`.",
            )
        st.markdown("</div>", unsafe_allow_html=True)
