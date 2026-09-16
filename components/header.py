import streamlit as st

from utils.style_helpers import logo_data_uri


def render_header():
    logo_uri = logo_data_uri()
    if logo_uri:
        emblem_html = f'<img src="{logo_uri}" class="tdi-logo-img" alt="Logo du Ministère des Finances et du Budget" />'
    else:
        # Aucun fichier réel déposé dans assets/ (voir assets/README.md) :
        # badge neutre en attendant le vrai logo, jamais un logo inventé.
        emblem_html = '<div class="tdi-logo-placeholder">MFB</div>'

    st.markdown(
        f"""
        <div class="tdi-header">
            <div class="tdi-header-left">
                {emblem_html}
                <span class="tdi-flag">🇹🇬</span>
                <div>
                    <div class="tdi-title">TOGO DIGITAL INTELLIGENCE</div>
                    <div class="tdi-subtitle">
                        Ministère des Finances et du Budget — Pilotage de l'économie numérique
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
