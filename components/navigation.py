from streamlit_option_menu import option_menu

# Maximum 6 entrees : la navigation reste un vrai bandeau de pilotage,
# pas un menu qui deborde. "Ecosysteme numerique" fusionne les anciennes
# sections Entreprises + Usages numeriques ; "A propos" est deplace dans
# le pied de page (voir components/footer.py) pour ne pas consommer un
# slot du menu principal.
SECTIONS = [
    "Accueil",
    "Vue nationale",
    "Territoires",
    "Infrastructures",
    "Écosystème numérique",
    "Indicateurs",
]

ICONS = [
    "house",
    "bar-chart-line",
    "geo-alt",
    "hdd-network",
    "diagram-3",
    "clipboard-data",
]


def render_navigation(default_index: int = 0) -> str:
    """Barre de navigation horizontale, dense et alignee sur la charte Togo."""
    return option_menu(
        menu_title=None,
        options=SECTIONS,
        icons=ICONS,
        default_index=default_index,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "3px",
                "background-color": "#FFFFFF",
                "border-radius": "12px",
                "box-shadow": "0 1px 3px rgba(11,31,51,0.06)",
            },
            "icon": {"color": "#334155", "font-size": "14px"},
            "nav-link": {
                "font-size": "13px",
                "font-weight": "600",
                "color": "#334155",
                "text-align": "center",
                "margin": "2px",
                "padding": "8px 16px",
                "border-radius": "9px",
            },
            "nav-link-selected": {
                "background-color": "#006A4E",
                "color": "#FFFFFF",
            },
        },
    )
