
import pygame
from config import TILE_SIZE, ADDED_SAFETY_TILES, MINIMAP_SIZE_DIVIDER, MINIMAP_PLAYER_SCALE, MINIMAP_PLAYER_COLOR
from assets_loader import assets
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

        for y, line in enumerate(ground):
            for x, tile in enumerate(line):
                big_minimap.blit(assets.get(tile), (x * tile_size_x, y * tile_size_y))
    
        minimap_size = (self.game.w / temp_factor, self.game.h / temp_factor)
        self.minimap = pygame.transform.smoothscale(big_minimap, minimap_size)
        self.minimap_position = (self.game.w - self.game.w / temp_factor, 0)
        self.minimap_tile_size = (tile_size_x, tile_size_y)

    def change_offset(self, *, dx: int = 0, dy: int = 0):
        self.offset_x = self.__clamp(self.offset_x + dx, -self.max_x, 0)
        self.offset_y = self.__clamp(self.offset_y + dy, -self.max_y, 0)

    def render_ground(self):
        """
        TODO: Optimize
        """

        """
        ground = self.game.world.ground
        for y, line in enumerate(ground):
            for x, tile in enumerate(line):
                self.game.screen.blit(assets.get(tile), (x * TILE_SIZE + self.offset_x, y * TILE_SIZE + self.offset_y))
        """

        
        ground = self.game.world.ground
        blocks = self.game.world.blocks_size
        x, max_x = -(self.offset_x // TILE_SIZE) - ADDED_SAFETY_TILES, -(self.offset_x // TILE_SIZE) + self.game.w // TILE_SIZE + ADDED_SAFETY_TILES
        y, max_y = -(self.offset_y // TILE_SIZE) - ADDED_SAFETY_TILES, -(self.offset_y // TILE_SIZE) + self.game.h // TILE_SIZE + ADDED_SAFETY_TILES
        remaining_offset_x, remaining_offset_y = self.offset_x % TILE_SIZE, self.offset_y % TILE_SIZE
        
        if x < 0:
            x = 0
        if max_x > blocks[0] - 1:
            max_x = blocks[0] - 1
        if y < 0:
            y = 0
        if max_y > blocks[1] - 1:
            max_y = blocks[1] - 1

        initial_x, initial_y = x, y
        
        while y <= max_y:
            while x <= max_x:
                self.game.screen.blit(
                    assets.get(ground[y][x]), # image de la tile
                    (
                        (x - initial_x - ADDED_SAFETY_TILES) * TILE_SIZE + remaining_offset_x, # position x de la tile 
                        (y - initial_y - ADDED_SAFETY_TILES) * TILE_SIZE + remaining_offset_y # position y de la tile
                    )
                )
                x += 1
            y += 1
            x = initial_x

    def render_player(self):
        pass # TODO: Make the render_player() method

    def render_minimap(self):
        self.game.screen.blit(self.minimap, self.minimap_position)
        player_rect_on_minimap = (
            self.minimap_position[0] - (((self.offset_x / TILE_SIZE) - (self.game.w / TILE_SIZE) / 2) * self.minimap_tile_size[0]) / MINIMAP_SIZE_DIVIDER - MINIMAP_PLAYER_SCALE / 2,
            self.minimap_position[1] - (((self.offset_y / TILE_SIZE) - (self.game.h / TILE_SIZE) / 2) * self.minimap_tile_size[1]) / MINIMAP_SIZE_DIVIDER - MINIMAP_PLAYER_SCALE / 2,
            # dans l'ordre :
            #   - self.minimap_position[0] et self.minimap_position[1] : pour ajouter la position de l'angle supérieur gauche de la minimap
            #   - self.offset_x / TILE_SIZE et self.offset_y / TILE_SIZE : pour obtenir les coordonées de la tile actuelle (par rapport au nombre total de tiles)
            #   - (self.game.w / TILE_SIZE) / 2 et (self.game.h / TILE_SIZE) / 2 pour que la position représente ce qui est au centre de l'écran et non l'angle supérieur gauche
            #   - *self_minimap_tile_size[0] et *self_minimap_tile_size[1] pour convertir les coordonnées de la tile en pixels
            #   - /MINIMAP_SIZE_DIVIDER pour mettre à l'échelle de la minimap
            #   - MINIMAP_PLAYER_SCALE / 2 parce qu'on dessine un rectangle, et en rtirant la moitié de sa taille on fait en sorte que son centre représente le milieu de l'écran
        )
        pygame.draw.rect(self.game.screen, MINIMAP_PLAYER_COLOR, (player_rect_on_minimap[0], player_rect_on_minimap[1], MINIMAP_PLAYER_SCALE, MINIMAP_PLAYER_SCALE))
        
    def render(self):
        self.game.screen.fill(("black"))
        self.render_ground()
        self.render_player()
        self.render_minimap()
