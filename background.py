import pygame
import math
from random import randint
from settings import *

class Background():
    def __init__(self):
        self.scroll = 0
        self.bgs = []
        self.floor1 = []

        # Load GAME-OVER Image
        self.game_over_img = pygame.image.load("assets/Background/game_over.png")

        # Load Background layers images:
        for z in range(1, 4):
            self.bgs.append(pygame.image.load(f"assets/Background/layer_{z}.png"))
            if z != 3:
                self.bgs[z - 1] = pygame.transform.scale(self.bgs[z - 1], (window_width, window_height))
            elif z == 3:
                self.bgs[z - 1] = pygame.transform.scale(self.bgs[z - 1], (window_width, self.bgs[z - 1].get_height()))

        # Load floor images
        for z in range(1, 5):
            self.floor1.append(pygame.image.load(f"assets/Tiles/floor_tile_{z}.png"))

    def drwaBG(self):
        for x in range(10):
            speed = 1
            for bg in self.bgs:
                if self.bgs.index(bg) != 2:
                    win.blit(bg, ((x * window_width) - self.scroll * speed, 0))
                    speed += 0.2
                elif self.bgs.index(bg) == 2:
                    win.blit(bg, ((x * window_width) - self.scroll * speed, window_height - 30))
                    speed += 0.2

    def draw_ground(self):
        floor_rnd = randint(1, 10)
        for z in range(1000):

            for x in range(1, 5):
                win.blit(self.floor1[x - 1], (
                x + z * (self.floor1[x - 1].get_width()) - self.scroll * 2.2, window_height - self.floor1[x - 1].get_height()))

    def draw_game_over(self):
        win.blit(self.game_over_img, (window_width/6, window_height/6))