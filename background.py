import pygame
import math

class Background():

    def __init__(self, x, y, width, height, speed):

        self.bg_images = [pygame.image.load('assets/Background/layer_1.png'), pygame.image.load('assets/Background/layer_2.png'), pygame.image.load('assets/Background/layer_3.png')]
        self.width = width
        self.height = height

        self.counter = 0
        self.bg_with_list = []
        self.tiles_list = []
        self.x_list = []
        self.y_list = []
        self.speed_list = []

        for items in self.bg_images:
            self.x_list.append(x)
            self.counter += 1
        self.counter = 0

        for items in self.bg_images:
            self.y_list.append(y)
            self.counter += 1
        self.counter = 0

        for bg in self.bg_images:
            self.bg_images[self.counter] = pygame.transform.scale(self.bg_images[self.counter], (width, height))
            self.counter += 1
        self.counter = 0

        for bg in self.bg_images:
            self.bg_with_list.append(self.bg_images[self.counter].get_width())
            self.counter += 1
        self.counter = 0

        for bg in self.bg_images:
            self.tiles_list.append(math.ceil(width / self.bg_with_list[self.counter]))
            self.counter += 1
        self.counter = 0

        self.width = width
        self.height = height
        self.speed = speed * 2



    def move(self, direction, max_width):

        for bg in self.bg_images:
            self.speed_list.append(self.speed + (self.counter + 1))
            #print(self.speed_list[self.counter])
            self.counter += 1
        self.counter = 0

        for bg in self.bg_images:
            self.x_list[self.counter] = self.x_list[self.counter] + (direction * self.speed_list[self.counter])
            print(self.x_list[self.counter])
            self.counter += 1
        self.counter = 0


