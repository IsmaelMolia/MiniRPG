import pygame
import time
from config import W, H, FPS, MAP_GROUND_FILE_PATH, MAP_DECORS_FILE_PATH, MAP_OBJECTS_PATH, CAMERA_SPEED


class Game:
    pass


from .world import World
from .rendering import Rendering


class Game:
    def __init__(self):
        self.playing = True

        self.w, self.h = W, H
        self.screen = pygame.display.set_mode((self.w, self.h))

        self.fps = FPS
        self.camera_speed = int(CAMERA_SPEED * (1000 / FPS))

        self.clock = pygame.time.Clock()
        self.delta = 0

        self.world = World(self, MAP_GROUND_FILE_PATH, MAP_DECORS_FILE_PATH, MAP_OBJECTS_PATH)

        # self.player = Player()
    
        self.rendering = Rendering(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rendering.change_offset(dx=-self.camera_speed)
        if keys[pygame.K_q]:
            self.rendering.change_offset(dx=self.camera_speed)
        if keys[pygame.K_s]:
            self.rendering.change_offset(dy=-self.camera_speed)
        if keys[pygame.K_z]:
            self.rendering.change_offset(dy=self.camera_speed)

    def loop(self):
        while self.playing:
            # logique jeu
            
            # boucle évènements
            self.check_events()

            # affichage
            self.rendering.render()
            pygame.display.update()

            # délai
            self.delta = self.clock.tick(self.fps)
            self.camera_speed = int(CAMERA_SPEED * self.delta)
            #print(self.delta)
            #print(self.camera_speed)

# les TODO ont étés déplacés dans 'documentation/todo.md'.
