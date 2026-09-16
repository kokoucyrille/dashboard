import streamlit as st

from components.charts import bar_chart, choropleth_map, empty_state, heatmap, section_title
from utils.data_loader import has_columns, load_geojson


def render(df, filters):
    section_title("Territoires", "Où se concentre l'activité numérique, et où se situent les plus fortes disparités ?")

    st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
    section_title("Carte du déficit numérique par préfecture", "")
    geojson = load_geojson("togo_prefectures.geojson")
    if geojson is not None and has_columns(df, ["prefecture", "score_deficit_numerique"]):
        fig = choropleth_map(
            geojson, df,
            locations="prefecture", featureidkey="properties.nom_prefecture",
            color="score_deficit_numerique", hover_name="prefecture",
        )
        st.plotly_chart(fig, width="stretch")
    elif has_columns(df, ["prefecture", "score_deficit_numerique"]):
        # Repli sans fond de carte : classement en barres tant que le GeoJSON n'est pas fourni
        agg = df.groupby("prefecture", as_index=False)["score_deficit_numerique"].mean()
        agg = agg.sort_values("score_deficit_numerique", ascending=False)
        st.plotly_chart(bar_chart(agg, x="prefecture", y="score_deficit_numerique"), width="stretch")
        st.caption("Fond de carte non fourni (data/togo_prefectures.geojson) — affichage en classement.")
    else:
        empty_state(
            "Carte territoriale",
            "Attendu : data/togo_prefectures.geojson + colonnes `prefecture`, `score_deficit_numerique`.",
        )
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Disparités région × indicateur", "Quels territoires cumulent le plus de faiblesses ?")
        if has_columns(df, ["region", "indicateur", "valeur"]):
            st.plotly_chart(heatmap(df, x="indicateur", y="region", z="valeur"), width="stretch")
        else:
            empty_state("Heatmap régionale", "Attendu : colonnes `region`, `indicateur`, `valeur`.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
        section_title("Classement des préfectures", "Quelles préfectures sont prioritaires ?")
        if has_columns(df, ["prefecture", "score_deficit_numerique"]):
            agg = df.groupby("prefecture", as_index=False)["score_deficit_numerique"].mean()
            agg = agg.sort_values("score_deficit_numerique", ascending=False).head(15)
            st.plotly_chart(bar_chart(agg, x="score_deficit_numerique", y="prefecture", orientation="h"), width="stretch")
        else:
            empty_state("Classement des préfectures", "Attendu : colonnes `prefecture`, `score_deficit_numerique`.")
        st.markdown("</div>", unsafe_allow_html=True)
