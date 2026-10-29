import pygame
from game.game import Game

def main():
    pygame.init()

    game = Game()
    game.loop()

    pygame.quit()

main()
