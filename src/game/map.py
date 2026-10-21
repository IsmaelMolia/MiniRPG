import pygame
import csv

class Map:
    def __init__(self, game):
        self.game = game

        self.ground_path = "assets_finaux/cartes/monde_sol.csv"

    def load_map(self):
        self.ground = []
        self.ground_images = {}
        with open(self.ground_path, "r") as f:
            for ligne in csv.reader(f):
                self.ground.append([])
                for tile in ligne:
                    #self.ground[-1].append(pygame.image.load(f"2_mini_rpg/assets_finaux/{tile}.png"))
                    self.ground[-1].append(tile)

                    if tile not in self.ground_images.keys():
                        self.ground_images[tile] = pygame.image.load(f"assets_finaux/{tile}.png")
                        self.ground_images[tile]

        self.tile_size_x, self.tile_size_y = self.game.w / len(self.ground[0]), self.game.h / len(self.ground)
        self.tile_positions = []
        for ligne in range(len(self.ground)):
            self.tile_positions.append([])
            for tile in range(len(self.ground[ligne])):
                #self.game.screen.blit(self.ground_images[self.ground[ligne][tile]], (size_x * tile, size_y * ligne, size_x, size_y))
                self.tile_positions[-1].append((self.tile_size_x * tile, self.tile_size_y * ligne, self.tile_size_x, self.tile_size_y))

        self.show_map()

    def show_map(self):
        #size_y = self.game.h / len(self.ground)
        #size_x = self.game.w / len(self.ground[0])

        for ligne in range(len(self.ground)):
            for tile in range(len(self.ground[ligne])):
                #self.ground[ligne][tile].blit(self.game.screen, (size_x * tile, size_y * ligne, size_x, size_y))
                #print(type(self.ground_images[self.ground[ligne][tile]]))
                #self.game.screen.blit(self.ground_images[self.ground[ligne][tile]], (size_x * tile, size_y * ligne, size_x, size_y))
                self.game.screen.blit(self.ground_images[self.ground[ligne][tile]], self.tile_positions[ligne][tile])
        