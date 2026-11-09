
import pygame
from config import MINIMAP_SIZE_DIVIDER, MINIMAP_TILES_LOADING_SIZE, TILE_SIZE, ADDED_SAFETY_TILES, MINIMAP_PLAYER_SCALE, MINIMAP_PLAYER_COLOR, MINIMAP_CAMERA_INDICATOR_WITDH
from assets_loader import assets
from ui.loading_bar import loading_bar_console
from .game import Game

class Rendering:
    def __init__(self, game: Game):
        self.game = game
        self.offset_x: int = 0
        self.offset_y: int = 0
        self.max_x = game.world.blocks_size[0] * TILE_SIZE - self.game.w
        self.max_y = game.world.blocks_size[1] * TILE_SIZE - self.game.h

        self.minimap: pygame.Surface | None = None

        self.compute_minimap()

    def __clamp(self, n: int | float, a: int | float, b: int | float):
        if n <= a:
            return a
        if n >= b:
            return b
        return n

    def compute_minimap(self):
        big_minimap = pygame.Surface((self.game.w, self.game.h))
        temp_factor = MINIMAP_SIZE_DIVIDER
    
        ground = self.game.world.ground
        blocks_number = self.game.world.blocks_size
        tile_size_x, tile_size_y = self.game.w / blocks_number[0], self.game.h / blocks_number[1]
        total_blocks = blocks_number[0] * blocks_number[1]

        tile_loading_size = MINIMAP_TILES_LOADING_SIZE
        for y, line in enumerate(ground):
            for x, tile in enumerate(line):
                #big_minimap.blit(assets.get(tile), (x * tile_size_x, y * tile_size_y))

                #big_minimap.blit(pygame.transform.smoothscale(assets.get(tile), (tile_loading_size, tile_loading_size)), (x * tile_size_x, y * tile_size_y))
                # blitting the images with a size of 8x8 (tile_loading_size = 8) is better because it takes a lot less time and it gives the same result.
                # -> if the images are blitted with their original size (64x64) or higher, it makes "big_minimap" contain much more information, 
                #    thus increasing the time it takes to create it by a lot.
                # -> if the images blitted are less than 8x8, they will be slightly cropped, and there will be black lines across the minimap. 

                #big_minimap.blit(assets.get_original(tile), (x * tile_size_x, y * tile_size_y))
                # if we directly load the original image instead of transforming a 1024x1024 image to a 8x8 (for example),
                # we gain a lot of performance.
                # it also makes that the minimap always takes the same time to load, no matter the TILE_SIZE.
                # the only problem is that it takes more memory, with AssetsLoader.assets_original_sizes.

                big_minimap.blit(pygame.transform.smoothscale(assets.get_original(tile), (tile_loading_size, tile_loading_size)), (x * tile_size_x, y * tile_size_y))
                # we can combine those 2 ideas (8x8 blit + original image) to improve performance even more.
                # this means that instead of having to do a pygame.transform.smoothscale() from a 1024x1024 to a 8x8 image (for example),
                # or blitting a 64x64 directly, we can transform.smoothscale() a 64x64 to a 8x8 and then .blit() it, which is way faster.
                # the only problem is that it takes more memory, with AssetsLoader.assets_original_sizes.
                
                loading_bar_console((x+1 + (y) * blocks_number[0])/total_blocks, "minimap")
    
        minimap_size = (self.game.w / temp_factor, self.game.h / temp_factor)
        self.minimap = pygame.transform.smoothscale(big_minimap, minimap_size)
        self.minimap_position = (self.game.w - self.game.w / temp_factor, 0)
        self.minimap_tile_size = (tile_size_x, tile_size_y) # to get the actual size in pixels it needs to be divided by MINIMAP_SIZE_DIVIDER.

    def change_offset(self, *, dx: int = 0, dy: int = 0):
        self.offset_x = self.__clamp(self.offset_x + dx, -self.max_x, 0)
        self.offset_y = self.__clamp(self.offset_y + dy, -self.max_y, 0)

    def render_ground(self):
        ground = self.game.world.ground
        blocks = self.game.world.blocks_size
        x, max_x = -(self.offset_x // TILE_SIZE) - ADDED_SAFETY_TILES, -(self.offset_x // TILE_SIZE) + self.game.w // TILE_SIZE + ADDED_SAFETY_TILES
        y, max_y = -(self.offset_y // TILE_SIZE) - ADDED_SAFETY_TILES, -(self.offset_y // TILE_SIZE) + self.game.h // TILE_SIZE + ADDED_SAFETY_TILES
        
        if x < 0:
            x = 0
        if max_x > blocks[0] - 1:
            max_x = blocks[0] - 1
        if y < 0:
            y = 0
        if max_y > blocks[1] - 1:
            max_y = blocks[1] - 1

        initial_x = x
        
        while y <= max_y:
            while x <= max_x:
                self.game.screen.blit(
                    assets.get(ground[y][x]), 
                    (
                        x * TILE_SIZE + self.offset_x,
                        y * TILE_SIZE + self.offset_y
                    )
                )
                x += 1
            y += 1
            x = initial_x

    def render_player(self):
        pass # TODO: Make the render_player() method

    def render_minimap(self):
        self.game.screen.blit(self.minimap, self.minimap_position)
        
        """
        player_rect_on_minimap = (
            self.minimap_position[0] - (((self.offset_x / TILE_SIZE) - (self.game.w / TILE_SIZE) / 2) * self.minimap_tile_size[0]) / MINIMAP_SIZE_DIVIDER - MINIMAP_PLAYER_SCALE / 2,
            self.minimap_position[1] - (((self.offset_y / TILE_SIZE) - (self.game.h / TILE_SIZE) / 2) * self.minimap_tile_size[1]) / MINIMAP_SIZE_DIVIDER - MINIMAP_PLAYER_SCALE / 2,
            # dans l'ordre :
            #   - self.minimap_position[0] et self.minimap_position[1] : pour ajouter la position de l'angle supérieur gauche de la minimap
            #   - self.offset_x / TILE_SIZE et self.offset_y / TILE_SIZE : pour obtenir les coordonées de la tile actuelle (par rapport au nombre total de tiles)
            #   - (self.game.w / TILE_SIZE) / 2 et (self.game.h / TILE_SIZE) / 2 pour que la position représente ce qui est au centre de l'écran et non l'angle supérieur gauche
            #   - *self_minimap_tile_size[0] et *self_minimap_tile_size[1] pour convertir les coordonnées de la tile en pixels
            #   - /MINIMAP_SIZE_DIVIDER pour mettre à l'échelle de la minimap
            #   - MINIMAP_PLAYER_SCALE / 2 parce qu'on dessine un rectangle, et en retirant la moitié de sa taille on fait en sorte que son centre représente le milieu de l'écran
        )
        pygame.draw.rect(self.game.screen, MINIMAP_PLAYER_COLOR, (player_rect_on_minimap[0], player_rect_on_minimap[1], MINIMAP_PLAYER_SCALE, MINIMAP_PLAYER_SCALE))
        """

        camera_rect_on_minimap = (
            self.minimap_position[0] - ((self.offset_x / TILE_SIZE - ADDED_SAFETY_TILES) * self.minimap_tile_size[0]) / MINIMAP_SIZE_DIVIDER,
            self.minimap_position[1] - ((self.offset_y / TILE_SIZE - ADDED_SAFETY_TILES) * self.minimap_tile_size[1]) / MINIMAP_SIZE_DIVIDER,
            ((self.game.w // TILE_SIZE + ADDED_SAFETY_TILES * 2) * self.minimap_tile_size[0]) / MINIMAP_SIZE_DIVIDER,
            ((self.game.h // TILE_SIZE + ADDED_SAFETY_TILES * 2) * self.minimap_tile_size[1]) / MINIMAP_SIZE_DIVIDER,
        )
        pygame.draw.rect(self.game.screen, MINIMAP_PLAYER_COLOR, camera_rect_on_minimap, width=MINIMAP_CAMERA_INDICATOR_WITDH)
        
    def render(self):
        self.game.screen.fill(("black"))
        self.render_ground()
        self.render_player()
        self.render_minimap()
