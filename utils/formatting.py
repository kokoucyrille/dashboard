"""Fonctions de formatage réutilisables pour KPI, graphiques et tableaux."""


def format_number(value, decimals: int = 0, suffix: str = "") -> str:
    """Formate un nombre en style FR (espace comme séparateur de milliers)."""
    if value is None:
        return "—"
    try:
        formatted = f"{value:,.{decimals}f}".replace(",", " ").replace(".", ",")
        return f"{formatted}{suffix}"
    except (TypeError, ValueError):
        return "—"


def format_percent(value, decimals: int = 1) -> str:
    if value is None:
        return "—"
    return format_number(value, decimals=decimals, suffix=" %")


def compute_delta_pct(current: float | None, previous: float | None):
    """Variation en % entre deux valeurs. Renvoie None si le calcul est impossible."""
    if current is None or previous in (None, 0):
        return None
    try:
        return ((current - previous) / previous) * 100
    except (TypeError, ZeroDivisionError):
        return None
