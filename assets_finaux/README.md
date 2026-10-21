# Assets finaux séparés

Ce dossier contient les images utilisées par le jeu, exportées en PNG individuels avec transparence, sans tilesets ni spritesheets.

## Carte

Les PNG à la racine portent exactement le nom des clés CSV, espaces et zéros compris : `grass 00.png`, `tree 06.png`, `rock 04.png`, `house 00.png`, etc. Toutes les variantes du catalogue sont présentes, même celles qui ne sont pas placées dans la carte actuelle.

Pour une case contenant `tree 06`, charger simplement `tree 06.png`. Une cellule vide ne correspond à aucune image.

- Les sols mesurent 64 × 64 pixels.
- Les objets sont à leur taille d'affichage dans le jeu ; leurs proportions et leur transparence sont conservées. Un bâtiment peut dépasser une case.
- Un objet se place avec le bas de son image au bas de la case, centré horizontalement.
- `catalogue.csv` associe chaque clé à son PNG local et à sa hauteur.
- `ressources.csv` conserve les propriétés des arbres et rochers.
- `cartes/` contient une copie des cartes CSV et des repères.

Les raccords entre variantes d'un même sol sont déjà appliqués : ne pas appliquer une seconde fois `preparer_textures` sur ces PNG. Les transitions entre matières différentes dépendent des cases voisines et restent calculées par `rendu_terrain.py` ; elles ne peuvent pas être représentées par un unique PNG par clé.

## Interface et cultures

`interface/` contient les icônes de ressources et d'outils, ainsi que les textures de terre sèche et humide des cultures. Les panneaux, jauges et pousses sont dessinés par le code du jeu.

## Personnage

`personnage/` contient une image de 64 × 64 pixels par pose et direction, avec les couleurs par défaut. Exemple : `personnage nord 01.png`. La marche vers le nord inclut la correction des pas.

| Numéro | Pose |
| --- | --- |
| 00 | Repos |
| 01 | Premier pas |
| 02 | Passage |
| 03 | Second pas |
| 04 | Préparation du coup |
| 05 | Impact |
| 06 | Récolte |
| 07 | Travail au sol |

`animations.json` donne l'ordre des poses (marche : 01, 02, 03, 02, à 8 images par seconde). Le bas-centre du personnage est au point (32, 61) de sa cellule.

`personnage/couches/` contient les cinq couches séparées pour chaque pose : corps, peau, cheveux, haut et bas. Les quatre couches colorables sont en niveaux de gris ; les multiplier par une couleur de `palettes.json`, puis les superposer au corps dans l'ordre peau, cheveux, haut, bas.

## Réexporter

Depuis le dossier du projet :

```powershell
.\.venv\Scripts\python.exe tools/exporter_assets_finaux.py
```

Cette commande actualise les PNG et CSV de cet export à partir des assets du jeu. Les anciens assets retirés du catalogue ne sont pas effacés automatiquement.
