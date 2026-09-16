import streamlit as st


def render_footer():
    st.markdown(
        """
        <div class="tdi-footer">
            <div class="tdi-footer-title">TOGO DIGITAL INTELLIGENCE</div>
            <div class="tdi-footer-motto">🇹🇬 Travail – Liberté – Patrie · Ministère des Finances et du Budget</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.expander("ℹ️ À propos & méthodologie", expanded=False):
        st.markdown(
            """
            <p style="color:#334155; font-size:13px; line-height:1.6; margin:0 0 8px 0;">
                Plateforme d'intelligence territoriale pour l'analyse et le suivi de
                l'économie numérique du Togo (connectivité, infrastructures télécoms,
                disparités territoriales).
            </p>
            <p style="color:#334155; font-size:13px; line-height:1.6; margin:0 0 8px 0;">
                <strong>Méthodologie</strong> : données issues exclusivement des jeux
                de données fournis au projet. Aucune valeur n'est générée
                artificiellement — une visualisation sans donnée disponible l'indique
                explicitement plutôt que de l'estimer.
            </p>
            <p style="color:#334155; font-size:13px; line-height:1.6; margin:0;">
                <strong>Conception</strong> : DAYO Kokou Cyrille — Étudiant en Master 1
                Big Data à l'UCAO-UUT, Ingénieur de Travaux Informatiques à la DGTCP.
            </p>
            """,
            unsafe_allow_html=True,
        )
