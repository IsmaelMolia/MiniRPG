from pygame import Surface, image

from config import ASSETS_PATH


class AssetsLoader:
    def __init__(self, assets_folder: str):
        self.assets_folder = assets_folder
        self.assets: dict[str, Surface] = {}

    def get(self, filename: str) -> Surface:
        if filename not in self.assets:
            self.assets[filename] = image.load(f'{self.assets_folder}/{filename}.png')
        return self.assets[filename]


assets = AssetsLoader(ASSETS_PATH)
