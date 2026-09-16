# TOGO DIGITAL INTELLIGENCE

Template Streamlit premium pour le pilotage de l'économie numérique du Togo —
navigation horizontale, filtres, KPI, graphiques Plotly, carte, storytelling
data-driven. Le template fonctionne dès maintenant, **sans données** : chaque
graphique affiche un état vide explicite tant que le fichier correspondant
n'est pas fourni (aucune donnée fictive n'est jamais générée).

## Installation

```bash
python -m venv .venv
source .venv/bin/activate       # Windows : .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Structure du projet

```
app.py                  Point d'entrée : header, navigation, routage des sections
components/              Briques réutilisables (header, footer, nav, filtres, KPI, graphiques)
sections/                Une fonction render() par section du menu
utils/                   Chargement de données, formatage, injection CSS
styles/custom.css        Design system (palette Togo, cartes, placeholders)
data/                    Dépose ici tes exports CSV/GeoJSON (voir data/README.md)
assets/                  Logo / drapeau optionnel
.streamlit/config.toml   Thème natif Streamlit (fallback)
```

## Brancher tes données

1. Dépose tes exports dans `data/` en suivant le schéma décrit dans
   `data/README.md` (basé sur les colonnes que ton notebook
   `Analyse_Economie_Numerique_Togo.ipynb` produit déjà : agences
   Moov/Togocom, agents Mobile Money, data centers, score de déficit
   numérique par préfecture).
2. Vérifie le nom de fichier attendu dans `app.py` :
   `load_csv("dataset_economie_numerique.csv")` — renomme-le si besoin.
3. Recharge l'application : les KPI, graphiques et filtres se remplissent
   automatiquement, section par section, sans autre modification de code.

## Personnalisation rapide

- **Couleurs / typographie** : `styles/custom.css` (variables CSS en tête de
  fichier).
- **Ajouter une section** : crée `sections/ma_section.py` avec une fonction
  `render(df, filters)`, ajoute-la à `SECTIONS` dans
  `components/navigation.py` et au routage dans `app.py`.
- **Ajouter un graphique** : ajoute une fonction dans `components/charts.py`
  (thème Plotly déjà appliqué via `_apply_theme`).

## Principe directeur

Le template est volontairement livré vide de données. C'est un squelette
prêt à l'emploi : dès que les fichiers réels arrivent, il devient le
dashboard analytique complet décrit dans le cahier des charges.
