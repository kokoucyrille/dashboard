# Schéma de données attendu

Ce dossier est **vide par conception** : le dashboard ne doit jamais afficher
de données fictives. Chaque section affiche un état vide explicite tant que
le fichier correspondant n'est pas déposé ici.

## Fichier principal — `dataset_economie_numerique.csv`

Table large, une ligne par (préfecture × année) idéalement. Toutes les
colonnes sont optionnelles : dépose ce que tu as réellement (probablement
les exports de `Analyse_Economie_Numerique_Togo.ipynb`), les sections qui
n'ont pas leurs colonnes resteront simplement en état vide.

| Colonne | Type | Utilisée par |
|---|---|---|
| `annee` | int | Vue nationale, Usages numériques |
| `region` | str | Vue nationale, Territoires, Infrastructures |
| `prefecture` | str | Territoires, Indicateurs |
| `secteur` | str | Entreprises, filtres |
| `indicateur` | str | Vue nationale, Indicateurs (format long) |
| `valeur` | float | Vue nationale, Indicateurs (associée à `indicateur`) |
| `score_deficit_numerique` | float | Territoires, Indicateurs |
| `nb_agences_moov` | int | Infrastructures, Entreprises |
| `nb_agences_togocom` | int | Infrastructures, Entreprises |
| `nb_agents_mobile_money` | int | Infrastructures, Usages numériques |
| `nb_data_centers` | int | Infrastructures |
| `nombre_entreprises` | int | Entreprises |
| `type_operateur` | str | Entreprises (Moov / Togocom / Mobile Money / Data Center) |
| `taux_usage_numerique` | float | Usages numériques |
| `population` | int | Infrastructures (relation infra/population) — absente du ZIP source initial, à ajouter si une source fiable est trouvée |
| `population_numerique` | int | KPI Accueil |
| `penetration_internet` | float | KPI Accueil |
| `entreprises_numeriques` | int | KPI Accueil |
| `emplois_numeriques` | int | KPI Accueil |

Si tes exports sont répartis dans plusieurs fichiers (un par source :
agences, mobile money, data centers...), le plus simple est de les fusionner
en un seul CSV large avant de le déposer ici. Si tu préfères garder des
fichiers séparés, adapte `utils/data_loader.py` pour charger et joindre
chaque fichier (la structure du projet est faite pour ça — un
`load_csv("xxx.csv")` par source, puis un merge dans `app.py`).

## Fond de carte — `togo_prefectures.geojson`

GeoJSON des préfectures du Togo. La propriété utilisée pour la jointure avec
la colonne `prefecture` est `properties.nom_prefecture` (voir
`components/charts.py::choropleth_map`, paramètre `featureidkey` —
adapte-le si le nom de la propriété diffère dans ton fichier).

## Important

**Ne jamais commiter de données fictives ou d'exemple dans ce dossier** —
le dashboard est conçu pour rester honnête sur ce qu'il peut réellement
afficher.
