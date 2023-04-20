import pygame
from settings import *
from random import randint

class Background1():

    def __init__(self):
        self.bgs = []
        self.floor1 = []
        self.width = window_width
        self.height = window_height
        self.scroll = 0


        for z in range(1,4):
            self.bgs.append(pygame.image.load(f"assets/Background/layer_{z}.png"))
            if z != 3:
                self.bgs[z-1] = pygame.transform.scale(self.bgs[z-1], (window_width, window_height))
            elif z == 3:
                self.bgs[z - 1] = pygame.transform.scale(self.bgs[z - 1], (window_width, self.bgs[z-1].get_height()))

        for z in range(1,5):
            self.floor1.append(pygame.image.load(f"assets/Tiles/floor_tile_{z}.png"))



