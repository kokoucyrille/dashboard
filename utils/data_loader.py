"""
Chargement des données du dashboard.

Règle du projet : ne JAMAIS générer de données fictives. Tant qu'un fichier
attendu n'existe pas dans data/, les fonctions renvoient None et les
composants d'affichage basculent automatiquement sur un état vide explicite
(voir components/charts.py -> empty_state()).

Dépose tes exports (CSV / GeoJSON) dans le dossier data/ en respectant les
noms de fichiers et le schéma décrits dans data/README.md : les sections
du dashboard les détecteront automatiquement, sans aucune modification de
code nécessaire.
"""
import json
from pathlib import Path

import pandas as pd
import streamlit as st

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


@st.cache_data(show_spinner=False)
def load_csv(filename: str) -> pd.DataFrame | None:
    """Charge un CSV depuis data/ s'il existe, sinon renvoie None."""
    path = DATA_DIR / filename
    if not path.exists():
        return None
    try:
        return pd.read_csv(path)
    except Exception:
        return None


@st.cache_data(show_spinner=False)
def load_geojson(filename: str) -> dict | None:
    """Charge un GeoJSON (régions/préfectures) depuis data/ s'il existe."""
    path = DATA_DIR / filename
    if not path.exists():
        return None
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def has_columns(df: pd.DataFrame | None, columns: list[str]) -> bool:
    """Vérifie que df n'est pas vide/None et contient bien les colonnes attendues."""
    if df is None or df.empty:
        return False
    return set(columns).issubset(df.columns)
