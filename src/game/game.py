import pygame
from config import W, H, FPS, TILE_SIZE
from .map import Map
from .world import World, Rendering

class Game:
    def __init__(self):
        self.playing = True

        self.w, self.h = W, H
        self.screen = pygame.display.set_mode((self.w, self.h))

        self.clock = pygame.time.Clock()
        self.delta = 0

        self.map = Map(self)
        #self.world = World(self)

        # self.player = Player()
    
        self.rendering = Rendering(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.map.change_position(0)
        elif keys[pygame.K_q]:
            self.map.change_position(0, coeff=-1)
        if keys[pygame.K_s]:
            self.map.change_position(1)
        elif keys[pygame.K_z]:
            self.map.change_position(1, coeff=-1)

    def loop(self):
        while self.playing:
            # logique jeu
            
            # boucle évènements
            self.check_events()

            # affichage
            #pygame.draw.rect(self.screen, "black", (0, 0, self.w, self.h))
            #self.screen.fill(("black"))
            #self.map.show_entire_map()
            #self.rendering.render()
            pygame.display.update()

            # délai
            self.delta = self.clock.tick(FPS)
            #print(self.delta)
