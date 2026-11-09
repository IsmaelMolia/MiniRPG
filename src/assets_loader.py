import pygame
import time

from config import ASSETS_PATH, ASSETS_SIZES
from ui.loading_bar import loading_bar_console


class AssetsLoader:
    def __init__(self, assets_folder: str, assets_sizes: str):
        self.assets_folder = assets_folder
        self.assets_sizes = assets_sizes
        self.assets: dict[str, pygame.Surface] = {}
        self.assets_original_sizes: dict[str, pygame.Surface] = {}

    def get(self, filename: str) -> pygame.Surface:
        if filename not in self.assets:
            self.assets[filename] = pygame.image.load(f'{self.assets_folder}/{filename}.png')
        return self.assets[filename]
    
    def get_with_size(self, filename: str, size: tuple[int]) -> pygame.Surface: 
        #'''If the asset is already in AssetsLoader.assets, its size won't change.'''
        '''If the asset is already in AssetsLoader.assets, its size will change. '''
        if filename not in self.assets:
            self.assets[filename] = pygame.image.load(f'{self.assets_folder}/{filename}.png')
        self.assets[filename] = pygame.transform.smoothscale(self.assets[filename], size)
        return self.assets[filename]

    def get_original(self, filename: str) -> pygame.Surface:
        '''Same as the .get() method but returns the asset with its original size (in the file it was loaded from).'''
        if filename not in self.assets_original_sizes:
            self.assets_original_sizes[filename] = pygame.image.load(f'{self.assets_folder}/{filename}.png')
        return self.assets_original_sizes[filename]

    def load_multiple_assets(self, filenames: list[str], size: tuple[int] | None, title: str | None) -> None:
        if size == None:
            size = (self.get(filenames[0])).get_size() # if size == None, the size of every image will be the default size of the first image
        
        if title != None:
            total_files = len(filenames)
            for index, f in enumerate(filenames):
                self.get_with_size(f, size)
                loading_bar_console((index+1)/total_files, title)
            return

        for f in filenames:
            self.get_with_size(f, size)
    
assets = AssetsLoader(ASSETS_PATH, ASSETS_SIZES)
