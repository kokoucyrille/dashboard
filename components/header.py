import streamlit as st


def render_header():
    st.markdown(
        """
        <div class="tdi-header">
            <div class="tdi-header-left">
                <span class="tdi-flag">🇹🇬</span>
                <div>
                    <div class="tdi-title">TOGO DIGITAL INTELLIGENCE</div>
                    <div class="tdi-subtitle">
                        Plateforme d'intelligence territoriale pour le pilotage
                        de l'économie numérique du Togo
                    </div>
                </div>
            </div>
            <div class="tdi-header-right">
                <span class="tdi-badge">Data Intelligence</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
