import pygame
from config import *
from game.map import Map

class Game:
    def __init__(self):
        self.playing = True

        self.w, self.h = W, H
        self.screen = pygame.display.set_mode((self.w, self.h))

        self.clock = pygame.time.Clock()
        self.delta = 0

        self.map = Map(self)
        self.map.load_map()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def game_loop(self):
        while self.playing:
            # logique jeu
            
            # boucle évènements
            self.check_events()

            # affichage
            #pygame.draw.rect(self.screen, "black", (0, 0, self.w, self.h))
            #self.screen.fill(("black"))
            #self.map.show_map()
            pygame.display.update()

            # délai
            self.delta = self.clock.tick(60)
            #print(self.delta)
