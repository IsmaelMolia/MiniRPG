Architecture :

Minirpg                         -> dossier qui contient le projet
    .venv                       -> dossier qui contient environnement virrtuel, à mettre dans le .gitignore
    assets_finaux               -> dossier qui contient assets du projet
    documentation               -> dossier qui contiendra des informations supplémentaires sur le projet
        idees.md                -> fichier qui contient liste de choses à faire/essayer
        infos_bonus.md          -> fichier qui sert à mieux comprendre la structure du projet
    scripts                     -> dossier qui contiendra les scripts hors python
    src                         -> dossier qui contient les scripts python
        game                    -> dossier qui contient les scripts uniquement liés au jeu
            game.py             -> fichier qui contient la classe Game (classe qui permet de faire la boucle de jeu, de gérer les inputs et de faire les autres classes interagir entre elles)
            player.py           -> fichier qui contient la classe Player (inhérite de la classe Entity, permet de stocker les données du joueur et de gérer ses actions)
            saves_handler.py    -> fichier qui contient la classe SavesHandler (permet de de créer, de stocker et de renvoyer les données de sauvegardes de l'utilisateur avec des fichiers .json)
            units.py            -> fichier qui contient la classe Entity (classe Parent qui permet de créer des entités, notamment le joueur) et qui contiendra les classes des autres créatures (animaux, monstres, peut-être même tous les objets avec lesquels on peut interagir)
            world.py            -> fichier qui contient la classe World (qui stocke les données du monde) et la classe Rendering (qui affiche une partie de ce qui est stocké par World)
        ui                      -> dossier qui contient tout ce qui est lié à l'UI
            [button.py ?]
            [button_handler.py ?]
            [page_handler.py ?]
            ui.py               -> fichier qui contient la classe UI (gère tout ce qui est lié à l'UI)
        assets_loader.py        -> fichier qui contient la classe AssetLoader (récupère et stocke les assets dans le dossier assets_finaux)
        config.py               -> fichier qui contient les constantes utilisées dans les autres scripts python
        main.py                 -> fichier qui permet de lancer le jeu
    .gitignore                  -> fichier qui permet de ne pas commit certains dossiers/fichiers
    README.md                   -> fichier qui contient des informations sur le projet
    requirements.txt            -> fichier qui indique les librairies nécessaires pour lancer le projet
