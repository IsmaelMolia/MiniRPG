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
        #self.map.load_entire_map()
        #self.map.show_entire_map()
        #"""
        self.map.load_current_zone()
        self.map.show_current_zone()
        self.map.load_minimap()
        self.map.show_minimap()
        self.map.show_position_on_minimap()
        #"""

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

    def game_loop(self):
        while self.playing:
            # logique jeu
            
            # boucle évènements
            self.check_events()

            # affichage
            #pygame.draw.rect(self.screen, "black", (0, 0, self.w, self.h))
            #self.screen.fill(("black"))
            #self.map.show_entire_map()
            pygame.display.update()

            # délai
            self.delta = self.clock.tick(60)
            print(self.delta)
