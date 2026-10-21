# Projet : RPG 2D pygame
## Liste d'idées non organisées :)

Pardon d'avance pour la lisibilité et la beauté de ce fichier
Pardon aussi pour mes explications mal organisées et parfois incompréhensibles

## [~] Étape 1 : Créer l'organisation du projet
### [~] étape 1.1 : setup
> 1. [X] Mettre en place un `environnement virtuel`, un .venv. On pourra utiliser "python3 -m venv .venv" dans la console de VS Code.
> 2. [ ] `Mettre en place git`, pour s'y retrouver plus tard, même si c'est un projet solo. Faire un `repository sur Github`, et le lier au projet. Je ne suis pas sûr, mais je pense qu'on pourra mettre le .venv dans le .gitignore, ainsi que certains dossiers futurs (comme data, par exemple)(et peut-être aussi assets ?).
### [X] étape 1.2 : structure dossiers et fichiers
> 1. [X] Pour l'instant, le projet aura `4 sous-dossiers` : `scripts`, `assets`, `documentation` et `data`. Les scripts seront dans le 1er, les assets open-source dans le 2eme, les fichiers .md pour s'aider dans le 3eme, les sauvegardes de l'utilisateur dans le 4eme (mais ce dossier n'a pas besoin d'être créé : il sera créé et géré par SaveHandler plus tard). 
> 2. [X] Dans les scripts, `chaque file aura son rôle`. On pourra créer `game.py`, qui contiendra la classe Game, base de la structure du jeu. Elle servira à relier les autres classes entre elles et à s'occuper de la game loop (logique jeu -> boucle évènements -> affichage -> délai), en appelant le code des classes correspondantes. Il y aura aussi `main.py`, qui servira simplement à lancer pygame (pygame.init()) ainsi que le programme principal (Game.game_loop()). On pourra ensuite ajouter les différentes parties qui feront marcher le jeu : `ui.py`, `saves_handler.py`, `player.py`, `map.py`, `units.py`, etc... Il faudra aussi ajouter `constants.py`, qui servira à stocker diverses variables arbitraires (ou au moins valeurs par défauts qui pourront être remplacées par SaveHandler).

## [ ] Étape 2 : Créer un menu
C'est sûrement une mauvaise décision, mais je veux commencer par créer un menu fonctionnel. Il faudra donc attendre avant de pouvoir commencer à coder et tester le jeu.
Il faudra bien structurer le code pour pouvoir facilement ajouter de nouvelles pages, faire des boutons personnalisés, pouvoir adapter l'UI selon la résolution de la fenêtre...
### [X] étape 2.1 : structure de base
> 1. [X] `créer 4 classes` -> `UI`, `PageHandler`, `ButtonHandler` et `Button`. Je réutilise les mêmes classes que pour mon jeu "`civ like pygame`". 
> 2. `UI` servira à regrouper `tout ce qui est lié à l'UI`, notamment les settings (par exemple, apparence par défaut d'un bouton dont les paramètres n'ont pas été spécifiés) et les autres classes. Peut-être qu'on pourra y ajouter d'autres fonctionnalités plus tard, pour le jeu. 
> 3. `PageHandler` servira à `connaître la page actuelle et afficher ce qui y correspond, en plus de gérer la logique` (la logique de la page principale, celle de la page qui gère les sauvgardes, celle de la page du jeu...). Il faudra séparer les "`pages principales`" (home, settings, sauvegarde...) des "`pages secondaires`" (pages qui peuvent s'afficher sur n'importe quelles pages principales, comme par exemple menu pause, inventaire ou minimap)(surtout utile en jeu).
> 4. `ButtonHandler` servira à `gérer les évènements liés à l'utilisation des boutons`, et sera utile notamment pour gérer les inputs (boutons à champ de texte), par exemple. 
> 5. `Button` servira à `créer les boutons`, et pour permettre de créer beaucoup de boutons différents, cette classe possèdera beacoup de variables : position, taille, couleur, survolable par la souris ou non (si oui, effet de zoom), inputable ou non (si oui, champ de texte apparaitra quand bouton clické)... Voici la liste de variables que j'avais utilisé dans `civ like pygame` : *self, button_handler, name, text, column, line, background_color, text_color, initial_size=1, zoom=BUTTON_ZOOM, roundness=BUTTON_ROUNDNESS, hoverable=True, clickable=True, inputable=False, special_value=None*. Il y avait évidemment + de variables totales, mais c'étaient celles du __init__.
### [ ] étape 2.2 : faire un début de menu
> 1. [ ] `Coder petit à petit les 4 classes`, toujours penser à comment sera la structure future pour `éviter des erreurs` qui seront visibles très tard et qui me feront recommencer le projet :(
> 2. [ ] Utiliser ce code pour créer la première page, avec quelques boutons basiques : `START` (pas encore codé), `SETTINGS` (qui dirige vers la 2eme page) et `EXIT` (assez explicite, facile à coder).
> 3. [ ] Rajouter des pages, rajouter des détails, essayer de rendre le tout joli. `Peaufiner ce menu basique`.
### étape 2.3 : créer un système de sauvegarde
> 1. [ ] Créer une classe `SavesHandler`. Elle sera la classe qui `crée et récupère les sauvegardes` et interagit avec les autres classes pour leur donner des informations. Pour l'instant, elle servira à sauvegarder les settings. Elle utilisera des librairies comme `os` et `pathlib` pour créer des dossiers et des fichiers, pour les chercher et les trouver peu importe l'emplacement du projet dans l'ordinateur. `Il faut que le projet soit déplaçable` dans l'ordinateur (ex : le changer de dossier). Pour les sauvegardes, on utilisera des fichiers `.json` ainsi que la bibliothèque `json` qui va avec.
> 2. [ ] Utiliser cette classe pour créer des paramètres de bases (résolution fenêtre pygame, couleur boutons, taille boutons, peut-être même contrôles dans le futur...) et faire en sorte de récupérer les `paths` pour rendre le projet déplaçable (surtout trouver le path du projet, on obtiendra ainsi les paths des sous-dossiers et des sous-fichiers).
> 3. [ ] Après avoir obtenu un menu assez satisfaisant (pages nécessaires, pas de bugs, optimisation), on pourra `créer la page du jeu`, qui aura une logique assez différente du menu. Pour l'instant, `faire un écran noir avec la possibilité de mettre en pause et de quitter`. Il faudra d'ailleurs `réfléchir au fonctionnement de la pause` pour le reste du jeu, elle sera un outil important.

## [ ] Étape 3 : Créer les bases du jeu
On peut maintenant se concentrer sur le principal du projet. On pourra réutiliser quelques éléments du menu, mais le défi principal sera de créer la logique du jeu, de bien gérer la structure du code, et de choisir comment sera le gameplay. Il faudra évidemment garder un maxiumum d'optimisation et un minimum de bugs.
### [ ] étape 3.1 : ??





## Idées bonus
> 1. [ ] Rajouter du son au jeu. Une musique, des effets sonores, juste assez pour rendre plus immersif. Je ne sais pas tout comment le faire ;)
> 2. [ ] Utiliser delta. La vitesse du jeu (écoulement temps, vitesse joueur, vitesse ennemis...) ne doit pas dépendre du nombre de frames par seconde.
