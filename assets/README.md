# Assets

## Logo du ministère

Dépose le vrai logo du **Ministère des Finances et du Budget** ici, sous
l'un de ces noms (le premier trouvé est utilisé) :

```
logo_ministere.svg
logo_ministere.png
logo_ministere.jpg
logo_ministere.jpeg
logo_ministere.webp
```

Il apparaîtra automatiquement dans le header dès le prochain
rechargement — aucune modification de code nécessaire
(`components/header.py` + `utils/style_helpers.py` s'en chargent).

Tant qu'aucun fichier réel n'est déposé, le header affiche un badge
neutre "MFB" à la place : jamais de logo inventé ou approximatif.

Recommandé : fond transparent, hauteur ≥ 120px pour un rendu net en SVG/PNG.

## Drapeau

L'emoji 🇹🇬 reste affiché à côté du logo. Pour le remplacer par un
visuel vectoriel, dépose `flag_togo.svg` et adapte `components/header.py`
de la même façon.
