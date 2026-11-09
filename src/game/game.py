import pygame
from config import W, H, FPS, TILE_SIZE, MAP_GROUND_FILE_PATH, CAMERA_SPEED


class Game:
    pass


from .world import World
from .rendering import Rendering


class Game:
    def __init__(self):
        self.playing = True

        self.w, self.h = W, H
        self.screen = pygame.display.set_mode((self.w, self.h))

        self.clock = pygame.time.Clock()
        self.delta = 0

        self.world = World(self, MAP_GROUND_FILE_PATH)

        # self.player = Player()
    
        self.rendering = Rendering(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rendering.change_offset(dx=-CAMERA_SPEED)
        if keys[pygame.K_q]:
            self.rendering.change_offset(dx=CAMERA_SPEED)
        if keys[pygame.K_s]:
            self.rendering.change_offset(dy=-CAMERA_SPEED)
        if keys[pygame.K_z]:
            self.rendering.change_offset(dy=CAMERA_SPEED)

    def loop(self):
        while self.playing:
            # logique jeu
            
            # boucle évènements
            self.check_events()

            # affichage
            #self.map.show_entire_map()
            self.rendering.render()
            pygame.display.update()

            # délai
            self.delta = self.clock.tick(FPS)
            #print(self.delta)


# TODO: pouvoir changer taille tiles (TILE_SIZE) sans bugs 
#       -> problème : assets_loader ne permet pas de changer leurs tailles ? ajouter une méthode qui s'en occupe quand map créée ?
# TODO: régler bugs render_ground()
# TODO: mettre format normal minimap ? (actuellement convertie pour avoir meme forme que l'ecran)
# TODO: vérifier que la position de joueur sur la minimap est la bonne, vérifier qu'il n'y a pas d'erreurs dans le calcul
# TODO: retirer 'ADDED_SAFETY_TILES' parce que cette variable n'a aucun sens ??
# TODO: à chaque fois que je fais un calcul compliqué, peut-être écrire son explication en commentaire ou dans la documentation ?
# TODO: peut-être mettre la taille de chaque asset dans ASSETS_SIZES pour ne pas avoir à le faire dans d'autres parties du code ?
# TODO: représenter le cadre de l'écran sur la minimap (plutôt que le centre de l'écran) (on rajoutera plus tard la position du joueur, qui ne sera pas forcément au centre de l'écran ?)
# TODO: pourquoi le chargement de la minimap devient + long quand TILE_SIZE est + élevé ?? ça devrait être l'inverse non ??
# TODO: dans rendering, à la fin de .compute_minimap(), il faudrait stocker minimap_tile_size avec sa vraie taille 
#       (et non sa taille au moment où elle a été utilisée sur big_minimap), et donc changer le code affecté par 'minimap_tile_size'