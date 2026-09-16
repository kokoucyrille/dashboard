import streamlit as st


def _options(df, column, default_label):
    """Renvoie les valeurs uniques triées d'une colonne, ou un placeholder si absente."""
    if df is not None and column in df.columns:
        values = sorted(v for v in df[column].dropna().unique())
        return [default_label] + list(values)
    return [default_label]


def render_filters(df=None) -> dict:
    """
    Rend les filtres analytiques. Les options se remplissent automatiquement
    dès qu'une colonne correspondante est présente dans le dataset chargé ;
    en attendant, chaque filtre reste visible mais n'affiche que son option
    par défaut (aucune valeur inventée).
    """
    st.markdown('<div class="tdi-filters-title">FILTRES</div>', unsafe_allow_html=True)

    if df is not None and "annee" in df.columns:
        years = sorted(int(y) for y in df["annee"].dropna().unique())
        year_range = st.select_slider(
            "📅 Année", options=years, value=(years[0], years[-1])
        )
    else:
        st.select_slider("📅 Année", options=["2020", "2025"], value=("2020", "2025"), disabled=True)
        year_range = None

    region = st.selectbox("📍 Région", _options(df, "region", "Toutes les régions"))
    prefecture = st.selectbox("🏛️ Préfecture", _options(df, "prefecture", "Toutes"))
    secteur = st.selectbox("💻 Secteur", _options(df, "secteur", "Tous"))
    indicateur = st.selectbox("📊 Indicateur", _options(df, "indicateur", "Tous"))

    reset = st.button("↻ Réinitialiser les filtres", width="stretch")
    if reset:
        st.rerun()

    return {
        "annee": year_range,
        "region": None if region.startswith("Toutes") else region,
        "prefecture": None if prefecture == "Tous" or prefecture == "Toutes" else prefecture,
        "secteur": None if secteur == "Tous" else secteur,
        "indicateur": None if indicateur == "Tous" else indicateur,
    }
