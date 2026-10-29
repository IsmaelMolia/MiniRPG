import pygame
import csv

from config import MAP_GROUND_FILE_PATH
from assets_loader import assets

class World:
    def __init__(self):
        self.ground: list[list[str]] = []
        self.size: tuple[int, int] = (-1, -1) # TODO: Cacl max map size
        '''In blocks'''
        #self.obstacles: list[Obstacles] = [] # TODO: Create Obstacles class
        #self.entities: list[Entity] = [] # TODO: Create Entity class

        self.load_ground()

    def load_ground(self):
        with open(MAP_GROUND_FILE_PATH, 'r') as f:
            for ligne in csv.reader(f):
                tiles = []
                for t in ligne:
                    tiles.append(t)
                self.ground.append(tiles)
            self.size = (len(self.ground[0]), len(self.ground)) # marche seulement avec une map rectangulaire

    def load_minimap(self):
        # load tout le reste puis rétrécir ??
        pass

class Rendering:
    def __init__(self, game: 'Game'):
        self.game = game
        self.offset_x: int = 0
        self.offset_y: int = 0
        self.max_x = 10240 # TODO: Calc max offset
        self.max_y = 10240 # TODO: Calc max offset

    def __clamp(self, n: int | float, a: int | float, b: int | float):
        if n <= a:
            return a
        if n >= b:
            return b
        return n

    def change_offset(self, *, dx: int = 0, dy: int = 0):
        self.offset_x = self.__clamp(self.offset_x + dx, 0, self.max_x)
        self.offset_y = self.__clamp(self.offset_y + dy, 0, self.max_y)

    def render(self):
        self.render_background()
        self.render_player()
        self.render_minimap()

    def render_background(self):
        ground = self.game.world.ground
        for y, line in enumerate(ground):
            for x, tile in enumerate(line):
                self.game.screen.blit(assets.get(tile), (x * TZS))



#from .game import Game
