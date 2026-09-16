import streamlit as st


def render_footer():
    st.markdown(
        """
        <div class="tdi-footer">
            <div class="tdi-footer-title">TOGO DIGITAL INTELLIGENCE</div>
            <div class="tdi-footer-sub">
                Plateforme d'intelligence territoriale pour le pilotage
                de l'économie numérique du Togo
            </div>
            <div class="tdi-footer-motto">🇹🇬 Travail – Liberté – Patrie</div>
            <div class="tdi-footer-tags">Data · Intelligence · Territoires</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
