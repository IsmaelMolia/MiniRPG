import pygame
import csv
from config import TILE_SIZE
from assets_loader import assets
from .game import Game


class World:
    def __init__(self, game: Game, ground_filepath: str, decors_filepath: str, objects_filepath: str):
        self.game = game

        self.filepaths = {
            'ground': ground_filepath,
            'decors': decors_filepath,
            'objects': objects_filepath,
        }

        self.world_storage = {
            'ground': [],       # list[list[str]]
            'objects': {},      # dict[tuple, str]
        }

        #self.obstacles: list[Obstacles] = [] # TODO: Create Obstacles class
        #self.entities: list[Entity] = [] # TODO: Create Entity class

        self.blocks_size: tuple[int, int] = (-1, -1) # computed with World.load_ground()
        '''In blocks'''

        self.load_things('ground')
        self.load_things('decors', 'ground')
        self.load_things('objects')
        self.blocks_size = (len(self.world_storage['ground'][0]), len(self.world_storage['ground']))

    def load_things(self, filepath_name: str, storage_name: str | None = None):
        filepath = self.filepaths[filepath_name]
        if storage_name == None:
            storage_name = filepath_name
        where_to_store = self.world_storage[storage_name]

        if type(where_to_store) == list:
            def store_element(storage: list, pos, element):
                '''
                This version of the function is for a list.
                - If the row (pos[1]) doesn't exist, a new row will be added.
                - If the element's index (pos[0] doesn't exist, it will be added to the last row.
                - But if the row and the element's index are within the list, the element will replace the value that is currently at this position. 
                '''
                if pos[1] < 0 or pos[1] >= len(storage):
                    storage.append([])
                if pos[0] < 0 or pos[0] >= len(storage[pos[1]]):
                    storage[-1].append(element)
                storage[pos[1]][pos[0]] = element
        elif type(where_to_store) == dict:
            def store_element(storage: dict, pos, element):
                '''
                This version of the function is for a dict. 
                - It only needs to set "pos" as the key and "element" as the value.
                '''
                storage[pos] = element

        filenames = []
        with open(filepath, 'r') as f:
            for iy, ligne in enumerate(csv.reader(f)):
                for ix, element in enumerate(ligne):
                    if len(element) > 1:
                        store_element(where_to_store, (ix, iy), element)
                        if element not in filenames:
                            filenames.append(element)

        assets.load_multiple_assets(filenames, (TILE_SIZE, TILE_SIZE), f'{filepath_name} assets')
