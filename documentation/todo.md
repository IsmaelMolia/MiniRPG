## Ce document sert à voir quelles choses à faire sont possibles, et ce ne sont que des propositions. Il y a des propositions de fixs, d'implémentations...
### Les TODO ne sont pas dans l'ordre dans lequel il faut les faire, ils sont juste organisés selon le moment où j'y ai pensé :)

Chaque TODO à 3 états :
- [ ] -> non fait
- [?] -> fait mais avec quelques différences ou quelques subtilités
- [x] -> fait

1. #### [x] TODO #1: 
* cases en 64x64
2. #### [ ] TODO #2: 
* essayer d'utiliser delta ?
3. #### [x] TODO #3: 
* pouvoir changer taille tiles (`TILE_SIZE`) sans bugs   
* problème : `assets_loader` ne permet pas de changer leurs tailles ? ajouter une méthode qui s'en occupe quand map créée ?
4. #### [x] TODO #4: 
* régler bugs `render_ground()`
5. #### [x] TODO #5: 
* mettre format normal minimap ? (actuellement convertie pour avoir meme forme que l'ecran)
* > plusieurs formats ajoutés
6. #### [?] TODO #6: 
* vérifier que la position de joueur sur la minimap est la bonne, vérifier qu'il n'y a pas d'erreurs dans le calcul
* >  position du 'joueur' (il n'y avait même pas de joueur, c'était juste le centre de l'écran) remplacé par indicateur de caméra
7. #### [ ] TODO #7: 
* retirer `ADDED_SAFETY_TILES` parce que cette variable n'a aucun sens ??
8. #### [ ] TODO #8: 
* à chaque fois que je fais un calcul compliqué, peut-être écrire son explication en commentaire ou dans la documentation ?
9. #### [?] TODO #9: 
* peut-être mettre la taille de chaque asset dans `ASSETS_SIZES` pour ne pas avoir à le faire dans d'autres parties du code ?
* > pas encore fait, est-ce qu'il y en aura besoin ou faut-il supprimer cette variable ?
10. #### [x] TODO #10: 
* représenter le cadre de l'écran sur la minimap (plutôt que le centre de l'écran) 
* (on rajoutera plus tard la position du joueur, qui ne sera pas forcément au centre de l'écran ?)
> fixed en même temps que le **TODO #6**
11. #### [x] TODO #11: 
* pourquoi le chargement de la minimap devient + long quand `TILE_SIZE` est + élevé ?? ça devrait être l'inverse non ??
> c'était parce que les tiles étaient d'abord affichées en très grand sur une surface temporaire puis rétrécies sur la minimap,
> et j'ai découvert que `pygame.transform.scale()` lag + quand le changement de taille est + important
12. #### [x] TODO #12: 
* dans rendering, à la fin de `.compute_minimap()`, il faudrait stocker `minimap_tile_size` avec sa vraie taille 
* (et non sa taille au moment où elle a été utilisée sur `big_minimap`), et donc changer le code affecté par `minimap_tile_size`
13. #### [x] TODO #13: 
* puisque que la minimap a maintenant un contour, il faudrait la décaler légérement pour voir tous les côtés de ce contour
14. #### [ ] TODO #14: 
* il faut vraiment modifier config.py, on ne peut pas se retrouver avec 200 variables à importer à la main dans chaque fichier...
15. #### [ ] TODO #15: 
* déplacer ces 'TODO' dans la documentation, même ceux réalisés, pour savoir quoi faire, pour garder une trace de ce qui a été fait et pour améliorer l'organisation
> avant, les 'TODO' étaient en commentaire à la fin du fichier *src/game.py*.
16. #### [x] TODO #16: 
* pour la minimap, mettre dans config une variable `MINIMAP_FORMAT` qui permet de décider si la minimap est du format de l'écran ou d'un carré, 
* et on pourra donc remplacer la taille de `big_minimap` par taile_x (=`self.game.w`) et taille_y (=`self.game.h` ou `self.game.w` selon format) et ensuite 
* utiliser ces variables dans la suite de `compute_minimap()`. On pourra ensuite créer la minimap différemment, par exemple en la construisant déjà petite, 
* car c'est un peu bizarre de la faire grande puis de la rétrécir. Cela permettra peut-être un gain de performance.
> tout a été fait, il y a maintenant différents formats de minimap et `compute_minimap()` a été optimisé.
> les formats sont des ratios, comme par exemple `(1, 0.75)` qui correspond à une longeur de ratio 1 et et une largeur de ratio 0.75 
> par exemple, le format `(1, 1)` donne une minimap de forme carrée
17. #### [ ] TODO #17: 
* quand `TILE_SIZE` est trop petite (donc quand les tiles ne remplissent pas tout l'écran), il y a des bugs. 
* Il faut soit fix ces bugs soit empêcher `TILE_SIZE` d'être plus petit que `self.game.w / self.blocks_size[0]` (par exemple)
18. #### [ ] TODO #18: 
* fix l'indicateur de camera, j'ai l'impression qu'il est affiché un peu trop à droite 
* (quand l'écran est centré sur un objet, l'indicateur montre que l'objet dépasse à gauche...)
* (très difficile à voir car différence de quelques pixels mais ce serait bien de savoir d'où vient le problème)

<br>
<br>

#### [ ] TODO #bonus:
* documentation à jour ?
> ce TODO est à part car il sert à savoir si la documentation est à jour ou non.
> il ne faut pas oublier de le décocher quand le code est modifié.