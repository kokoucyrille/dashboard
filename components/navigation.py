from streamlit_option_menu import option_menu

SECTIONS = [
    "Accueil",
    "Vue nationale",
    "Territoires",
    "Infrastructures",
    "Entreprises",
    "Usages numériques",
    "Indicateurs",
    "À propos",
]

ICONS = [
    "house",
    "bar-chart-line",
    "geo-alt",
    "hdd-network",
    "building",
    "phone",
    "clipboard-data",
    "info-circle",
]


def render_navigation(default_index: int = 0) -> str:
    """Barre de navigation horizontale, discrète et alignée sur la charte Togo."""
    return option_menu(
        menu_title=None,
        options=SECTIONS,
        icons=ICONS,
        default_index=default_index,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "4px",
                "background-color": "#FFFFFF",
                "border-radius": "14px",
                "box-shadow": "0 1px 3px rgba(11,31,51,0.06)",
            },
            "icon": {"color": "#334155", "font-size": "14px"},
            "nav-link": {
                "font-size": "13px",
                "font-weight": "600",
                "color": "#334155",
                "text-align": "center",
                "margin": "2px",
                "padding": "10px 14px",
                "border-radius": "10px",
            },
            "nav-link-selected": {
                "background-color": "#006A4E",
                "color": "#FFFFFF",
            },
        },
    )
