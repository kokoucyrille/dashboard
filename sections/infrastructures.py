import streamlit as st

from components.charts import bar_chart, empty_state, scatter_chart, section_title
from utils.data_loader import has_columns

INFRA_COLUMNS = [
    ("nb_agences_moov", "Agences Moov"),
    ("nb_agences_togocom", "Agences Togocom"),
    ("nb_agents_mobile_money", "Agents Mobile Money"),
    ("nb_data_centers", "Data Centers"),
]


def render(df, filters):
    section_title("Infrastructures numériques", "Quelle est la répartition des infrastructures télécoms sur le territoire ?")

    st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
    section_title("Répartition des infrastructures par région", "")
    present_cols = [c for c, _ in INFRA_COLUMNS if df is not None and c in df.columns]
    if present_cols and has_columns(df, ["region"]):
        agg = df.groupby("region", as_index=False)[present_cols].sum()
        long_df = agg.melt(id_vars="region", var_name="type_infrastructure", value_name="nombre")
        st.plotly_chart(bar_chart(long_df, x="region", y="nombre", color="type_infrastructure"), width="stretch")
    else:
        empty_state(
            "Infrastructures par région",
            "Attendu : colonne `region` + une ou plusieurs colonnes parmi "
            "`nb_agences_moov`, `nb_agences_togocom`, `nb_agents_mobile_money`, `nb_data_centers`.",
        )
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Infrastructures vs population", "L'implantation suit-elle la démographie ?")
        if has_columns(df, ["population", "nb_agences_moov"]) or has_columns(df, ["population", "nb_agences_togocom"]):
            infra_col = "nb_agences_moov" if "nb_agences_moov" in df.columns else "nb_agences_togocom"
            st.plotly_chart(
                scatter_chart(df, x="population", y=infra_col, hover_name=df.columns[0] if len(df.columns) else None),
                width="stretch",
            )
        else:
            empty_state(
                "Relation infrastructures / population",
                "Attendu : colonne `population` (non présente dans le ZIP source actuel — à ajouter si disponible).",
            )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Top préfectures équipées", "Où l'équipement est-il le plus dense ?")
        if present_cols and has_columns(df, ["prefecture"]):
            df_copy = df.copy()
            df_copy["total_infrastructures"] = df_copy[present_cols].sum(axis=1)
            agg = df_copy.groupby("prefecture", as_index=False)["total_infrastructures"].sum()
            agg = agg.sort_values("total_infrastructures", ascending=False).head(15)
            st.plotly_chart(bar_chart(agg, x="total_infrastructures", y="prefecture", orientation="h"), width="stretch")
        else:
            empty_state("Top préfectures équipées", "Attendu : colonne `prefecture` + colonnes d'infrastructures.")
        st.markdown("</div>", unsafe_allow_html=True)
