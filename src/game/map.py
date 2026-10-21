import pygame
import csv

class Map:
    def __init__(self, game):
        self.game = game

        self.temp_assets_path = "assets_finaux"
        self.ground_path = f"{self.temp_assets_path}/cartes/monde_sol.csv"

        self.temp_position = [200, 100]

    def change_position(self, axis=0, modifier=1, coeff=1):
        self.temp_position[axis] += modifier * coeff

        self.load_current_zone()
        self.show_current_zone()
        self.show_minimap()
        self.show_position_on_minimap()

    def load_entire_map(self):
        self.ground = []
        self.ground_images = {}
        with open(self.ground_path, "r") as f:
            for ligne in csv.reader(f):
                self.ground.append([])
                for tile in ligne:
                    #self.ground[-1].append(pygame.image.load(f"2_mini_rpg/assets_finaux/{tile}.png"))
                    self.ground[-1].append(tile)

                    if tile not in self.ground_images.keys():
                        self.ground_images[tile] = pygame.image.load(f"{self.temp_assets_path}/{tile}.png")
                        self.ground_images[tile]

        self.tile_size_x, self.tile_size_y = self.game.w / len(self.ground[0]), self.game.h / len(self.ground)
        self.tile_positions = []
        for ligne in range(len(self.ground)):
            self.tile_positions.append([])
            for tile in range(len(self.ground[ligne])):
                #self.game.screen.blit(self.ground_images[self.ground[ligne][tile]], (size_x * tile, size_y * ligne, size_x, size_y))
                self.tile_positions[-1].append((self.tile_size_x * tile, self.tile_size_y * ligne, self.tile_size_x, self.tile_size_y))

        #self.show_entire_map()

    def show_entire_map(self):
        #size_y = self.game.h / len(self.ground)
        #size_x = self.game.w / len(self.ground[0])

        for ligne in range(len(self.ground)):
            for tile in range(len(self.ground[ligne])):
                #self.ground[ligne][tile].blit(self.game.screen, (size_x * tile, size_y * ligne, size_x, size_y))
                #print(type(self.ground_images[self.ground[ligne][tile]]))
                #self.game.screen.blit(self.ground_images[self.ground[ligne][tile]], (size_x * tile, size_y * ligne, size_x, size_y))
                self.game.screen.blit(self.ground_images[self.ground[ligne][tile]], self.tile_positions[ligne][tile])

    def load_minimap(self):
        temp_coeff = 6

        self.minimap_ground = []
        self.minimap_ground_images = {}
        with open(self.ground_path, "r") as f:
            for ligne in csv.reader(f):
                self.minimap_ground.append([])
                for tile in ligne:
                    #self.ground[-1].append(pygame.image.load(f"2_mini_rpg/assets_finaux/{tile}.png"))
                    self.minimap_ground[-1].append(tile)

                    if tile not in self.minimap_ground_images.keys():
                        self.minimap_ground_images[tile] = pygame.image.load(f"{self.temp_assets_path}/{tile}.png")
                        #self.minimap_ground_images[tile] = pygame.transform.scale_by(self.minimap_ground_images[tile], (1/temp_coeff, 1/temp_coeff))
                        image_size = self.minimap_ground_images[tile].get_size()
                        self.minimap_ground_images[tile] = pygame.transform.smoothscale(self.minimap_ground_images[tile], (image_size[0]/temp_coeff, image_size[1]/temp_coeff))

        self.minimap_left, self.minimap_top = self.game.w - self.game.w / temp_coeff, 0
        self.minimap_tile_size_x, self.minimap_tile_size_y = (self.game.w / len(self.minimap_ground[0])) / temp_coeff, (self.game.h / len(self.minimap_ground)) / temp_coeff
        self.minimap_tile_positions = []
        for ligne in range(len(self.minimap_ground)):
            self.minimap_tile_positions.append([])
            for tile in range(len(self.minimap_ground[ligne])):
                self.minimap_tile_positions[-1].append((self.minimap_left + self.minimap_tile_size_x * tile, self.minimap_top + self.minimap_tile_size_y * ligne, self.minimap_tile_size_x, self.minimap_tile_size_y))

        #self.show_minimap()

    def show_minimap(self):
        for ligne in range(len(self.minimap_ground)):
            for tile in range(len(self.minimap_ground[ligne])):
                self.game.screen.blit(self.minimap_ground_images[self.minimap_ground[ligne][tile]], self.minimap_tile_positions[ligne][tile])

    def show_position_on_minimap(self):
        if (self.temp_position[0] > 0) and (self.temp_position[0] < len(self.ground[0])) and (self.temp_position[1] > 0) and (self.temp_position[1] < len(self.ground)):
            size = self.minimap_ground_images[self.minimap_ground[self.temp_position[1]][self.temp_position[0]]].get_size()
            pygame.draw.rect(self.game.screen, "red", (self.minimap_tile_positions[self.temp_position[1]][self.temp_position[0]][0], self.minimap_tile_positions[self.temp_position[1]][self.temp_position[0]][1], size[0], size[1]))

    def load_current_zone(self):
        self.load_entire_map() # si jamais on n'a pas load self.ground_images, self.ground et self.tile_positions

        temp_radius = 4
        upper_left_corner = (self.temp_position[0] - temp_radius, self.temp_position[1] - temp_radius)

        self.current_zone_global_positions = []  
        for y in range(temp_radius * 2 + 1):
            for x in range(temp_radius * 2 + 1):
                tile_pos = (upper_left_corner[0] + x, upper_left_corner[1] + y)
                if (tile_pos[0] > 0) and (tile_pos[0] < len(self.ground[0])) and (tile_pos[1] > 0) and (tile_pos[1] < len(self.ground)):
                    self.current_zone_global_positions.append(tile_pos)

        self.current_zone_local_positions = []
        tile_width, tile_height = self.game.w / (temp_radius * 2), self.game.h / (temp_radius * 2)

        for key, value in self.ground_images.items():
            self.ground_images[key] = pygame.transform.scale(value, (tile_width, tile_height))

        for y in range(temp_radius * 2 + 1):
            for x in range(temp_radius * 2 + 1):
                tile_pos = (tile_width * x, tile_height * y)
                self.current_zone_local_positions.append(tile_pos)

    def show_current_zone(self):
        self.game.screen.fill("black")
        for p in range(len(self.current_zone_global_positions)):
            self.game.screen.blit(\
                self.ground_images[self.ground[self.current_zone_global_positions[p][1]][self.current_zone_global_positions[p][0]]], \
                self.current_zone_local_positions[p]\
                        )

# optimisation ???
# -> pour ne pas avoir à reload toute la minimap, peut-etre ne pas afficher les tiles qui passeraient par dessus la minimap ?
# afficher toutes les cases en 64x64, ne pas les faire dependre de temp_radius
# combiner images en une seule surface (pour minimap)
