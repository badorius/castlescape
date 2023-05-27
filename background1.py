import pygame
import math
from random import randint
from settings import *
import threading
import os


class Background1():
    def __init__(self, level):
        self.scroll = 0
        self.bgs = []
        self.floor1 = []
        self.level = level
        self.images = []

        # specify the img directory path
        path = f"assets/Background/{self.level}/"
        # list files in img directory
        files = os.listdir(path)
        for file in files:
            # make sure file is an image
            if file.endswith(('.jpg', '.png', 'jpeg')):
                img_path = path + file
                self.images.append(img_path)

        for z in range(len(self.images)):
            self.bgs.append(pygame.image.load(self.images[z]).convert_alpha())

        # Load floor images
        #for z in range(1, 5):
        #    self.floor1.append(pygame.image.load(f"assets/Tiles/floor_tile_{z}.png").convert_alpha())

    def drwaBG(self):
        for x in range(10):
            speed = 1
            for bg in self.bgs:
                if self.bgs.index(bg) != (len(self.bgs) - 1):
                    win.blit(bg, ((x * window_width) - self.scroll * speed, 0))
                    speed += 0.1
                elif self.bgs.index(bg) == 2:
                    win.blit(bg, ((x * window_width) - self.scroll * speed, window_height - 30))
                    speed += 0.1

    def reset(self, level):
        self.level = level
        self.scroll = 0
        self.bgs = []
        self.floor1 = []

        for z in range(1, 4):
            self.bgs.append(pygame.image.load(f"assets/Background/{self.level}/layer_{z}.png").convert_alpha())
            if z != 3:
                self.bgs[z - 1] = pygame.transform.scale(self.bgs[z - 1], (window_width, window_height))
            elif z == 3:
                self.bgs[z - 1] = pygame.transform.scale(self.bgs[z - 1], (window_width, self.bgs[z - 1].get_height()))
