import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

PALETTE = ["#006A4E", "#FFCE00", "#0B1F33", "#D21034", "#4C9A82", "#8FA6BC"]

PLOTLY_LAYOUT = dict(
    font_family="Inter, sans-serif",
    font_color="#334155",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    colorway=PALETTE,
    margin=dict(l=10, r=10, t=30, b=10),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    hoverlabel=dict(bgcolor="#0B1F33", font_color="white", font_family="Inter"),
)

# Hauteur par défaut des graphiques : uniforme pour un vrai rendu "dashboard"
# (grille régulière, pas de cartes à hauteurs disparates).
DEFAULT_CHART_HEIGHT = 340


def _apply_theme(fig: go.Figure, height: int = DEFAULT_CHART_HEIGHT) -> go.Figure:
    fig.update_layout(**PLOTLY_LAYOUT, height=height)
    fig.update_xaxes(gridcolor="#EEF1F5", zeroline=False)
    fig.update_yaxes(gridcolor="#EEF1F5", zeroline=False)
    return fig


def section_title(title: str, question: str | None = None):
    st.markdown(f'<div class="tdi-section-title">{title}</div>', unsafe_allow_html=True)
    if question:
        st.markdown(f'<div class="tdi-section-question">{question}</div>', unsafe_allow_html=True)


def insight(text: str):
    """Commentaire analytique — ne doit être appelé qu'avec un texte calculé depuis les données."""
    st.markdown(f'<div class="tdi-insight">💡 {text}</div>', unsafe_allow_html=True)


def empty_state(question: str, detail: str = ""):
    """
    Placeholder affiché tant que les données nécessaires ne sont pas chargées.
    Remplace le graphique — jamais de valeurs inventées.
    """
    st.markdown(
        f"""
        <div class="tdi-empty-state">
            <div class="tdi-empty-icon">📭</div>
            <div class="tdi-empty-title">{question}</div>
            <div class="tdi-empty-text">
                {detail or "Cette visualisation s'affichera automatiquement dès que "
                            "le fichier de données correspondant sera déposé dans data/ "
                            "(voir data/README.md pour le schéma attendu)."}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def line_chart(df, x, y, color=None, title=""):
    fig = px.line(df, x=x, y=y, color=color, markers=True, title=title)
    return _apply_theme(fig)


def bar_chart(df, x, y, color=None, title="", orientation="v"):
    fig = px.bar(df, x=x, y=y, color=color, title=title, orientation=orientation)
    return _apply_theme(fig)


def donut_chart(df, names, values, title=""):
    fig = px.pie(df, names=names, values=values, hole=0.55, title=title)
    fig.update_traces(textposition="outside", textinfo="percent+label")
    return _apply_theme(fig)


def heatmap(df, x, y, z, title=""):
    fig = px.density_heatmap(
        df, x=x, y=y, z=z, histfunc="avg", title=title,
        color_continuous_scale=["#F5F7FA", "#4C9A82", "#006A4E"],
    )
    return _apply_theme(fig)


def scatter_chart(df, x, y, color=None, size=None, hover_name=None, title=""):
    fig = px.scatter(
        df, x=x, y=y, color=color, size=size, hover_name=hover_name,
        title=title, trendline=None,
    )
    return _apply_theme(fig)


def choropleth_map(geojson, df, locations, featureidkey, color, hover_name=None, title=""):
    fig = px.choropleth_mapbox(
        df,
        geojson=geojson,
        locations=locations,
        featureidkey=featureidkey,
        color=color,
        hover_name=hover_name,
        mapbox_style="carto-positron",
        center={"lat": 8.62, "lon": 0.83},  # centre approximatif du Togo
        zoom=6,
        opacity=0.75,
        title=title,
        color_continuous_scale=["#F5F7FA", "#4C9A82", "#006A4E"],
    )
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    return _apply_theme(fig, height=460)


def gauge(value, title="", max_value=100):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": title, "font": {"size": 13}},
            gauge={
                "axis": {"range": [0, max_value]},
                "bar": {"color": "#006A4E"},
                "bgcolor": "#F5F7FA",
                "steps": [
                    {"range": [0, max_value * 0.4], "color": "#FDEAEA"},
                    {"range": [max_value * 0.4, max_value * 0.7], "color": "#FFF6D6"},
                    {"range": [max_value * 0.7, max_value], "color": "#E3F1EC"},
                ],
            },
        )
    )
    return _apply_theme(fig)
