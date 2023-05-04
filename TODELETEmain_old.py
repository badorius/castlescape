import pygame
from game import Game

pygame.init()
pygame.display.set_caption("Castle Scape Game")

game = Game()
game.run_game_loop()

pygame.quit()
quit()