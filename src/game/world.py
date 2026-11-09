import pygame
import csv
from config import TILE_SIZE
from assets_loader import assets
from .game import Game


class World:
    def __init__(self, game: Game, ground_filepath: str):
        self.game = game
        self.ground_filepath = ground_filepath

        self.ground: list[list[str]] = []
        '''Contains ground assets name'''
        self.blocks_size: tuple[int, int] = (-1, -1) # computed with World.load_ground()
        '''In blocks'''
        #self.obstacles: list[Obstacles] = [] # TODO: Create Obstacles class
        #self.entities: list[Entity] = [] # TODO: Create Entity class

        self.load_ground()

    def load_ground(self):
        filenames = []
        with open(self.ground_filepath, 'r') as f:
            for ligne in csv.reader(f):
                tiles = []
                for t in ligne:
                    tiles.append(t)
                    if t not in filenames:
                        filenames.append(t)
                self.ground.append(tiles)
            self.blocks_size = (len(self.ground[0]), len(self.ground)) # marche seulement avec une map rectangulaire

        assets.load_multiple_assets(filenames, (TILE_SIZE, TILE_SIZE), 'ground assets')
