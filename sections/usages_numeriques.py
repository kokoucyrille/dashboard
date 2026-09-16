import streamlit as st

from components.charts import empty_state, insight, line_chart, scatter_chart, section_title
from utils.data_loader import has_columns
from utils.formatting import compute_delta_pct


def render(df, filters):
    section_title("Usages numériques", "Comment les usages numériques évoluent-ils, et sont-ils liés aux infrastructures ?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Évolution des usages", "L'usage progresse-t-il dans le temps ?")
        if has_columns(df, ["annee", "taux_usage_numerique"]):
            agg = df.groupby("annee", as_index=False)["taux_usage_numerique"].mean()
            st.plotly_chart(line_chart(agg, x="annee", y="taux_usage_numerique"), width="stretch")
            delta = compute_delta_pct(
                agg["taux_usage_numerique"].iloc[-1], agg["taux_usage_numerique"].iloc[0]
            )
            if delta is not None:
                direction = "accéléré" if delta >= 0 else "ralenti"
                insight(f"L'usage numérique a {direction} de {abs(delta):.1f} % sur la période observée.")
        else:
            empty_state("Évolution des usages", "Attendu : colonnes `annee`, `taux_usage_numerique`.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Infrastructures vs usages", "Existe-t-il une relation entre infrastructures et usages ?")
        if has_columns(df, ["nb_agents_mobile_money", "taux_usage_numerique"]):
            st.plotly_chart(
                scatter_chart(df, x="nb_agents_mobile_money", y="taux_usage_numerique", color="region" if "region" in df.columns else None),
                width="stretch",
            )
        else:
            empty_state(
                "Relation infrastructures / usages",
                "Attendu : colonnes `nb_agents_mobile_money`, `taux_usage_numerique`.",
            )
        st.markdown("</div>", unsafe_allow_html=True)
