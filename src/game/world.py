import pygame
import csv


class World:
    def __init__(self, game, ground_filepath: str):
        self.game = game
        self.ground_filepath = ground_filepath

        self.ground: list[list[str]] = []
        '''Contains ground assets name'''
        self.blocks_size: tuple[int, int] = (-1, -1) # computed with World.load_ground()
        '''In blocks'''
        #self.obstacles: list[Obstacles] = [] # TODO: Create Obstacles class
        #self.entities: list[Entity] = [] # TODO: Create Entity class

        #self.minimap: pygame.Surface | None = None

        self.load_ground()

    def load_ground(self):
        with open(self.ground_filepath, 'r') as f:
            for ligne in csv.reader(f):
                tiles = []
                for t in ligne:
                    tiles.append(t)
                self.ground.append(tiles)
            self.blocks_size = (len(self.ground[0]), len(self.ground)) # marche seulement avec une map rectangulaire

    #def compute_minimap(self):
        #self.minimap = pygame.Surface(self.blocks_size)

