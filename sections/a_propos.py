import streamlit as st


def render(df):
    st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="tdi-section-title">TOGO DIGITAL INTELLIGENCE</div>
        <p style="color:#334155; font-size:13.5px; line-height:1.7; max-width:780px;">
            Plateforme d'intelligence territoriale dédiée à l'analyse et au suivi de
            l'économie numérique du Togo. Elle rassemble les indicateurs de
            connectivité, d'infrastructures télécoms (agences Moov, Togocom, agents
            Mobile Money, data centers) et de disparités territoriales, afin d'aider
            décideurs, chercheurs et institutions à identifier les zones prioritaires
            et à suivre la progression de la transformation numérique du pays.
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="tdi-section-title" style="font-size:15px;">Concepteur</div>
        <p style="color:#334155; font-size:13px; line-height:1.6;">
            DAYO Kokou Cyrille — Étudiant en Master 1 à l'UCAO-UUT.
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="tdi-chart-card">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="tdi-section-title" style="font-size:15px;">Méthodologie</div>
        <p style="color:#334155; font-size:13px; line-height:1.6;">
            Les données affichées proviennent exclusivement des jeux de données
            fournis au projet, après audit et nettoyage. Aucune valeur n'est
            générée artificiellement : lorsqu'une donnée nécessaire à une
            visualisation n'est pas disponible, la plateforme l'indique
            explicitement plutôt que de l'estimer.
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
