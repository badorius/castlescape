import pygame
import math

class Background():

    def __init__(self, x, y, width, height, speed):
        self.bg_images = []
        self.width = width
        self.height = height
        self.bg_with_list = []
        self.tiles_list = []
        self.x_list = []
        self.y_list = []
        self.speed_list = []
        self.speed = speed * 2
        self.bg_num = 3

        for i in range(0,self.bg_num):
            self.bg_image = pygame.image.load(f"assets/Background/layer_{i+1}.png").convert_alpha()
            self.bg_images.append(self.bg_image)
            self.x_list.append(x)
            self.y_list.append(y)
            self.bg_images[i] = pygame.transform.scale(self.bg_images[i], (width, height))
            self.bg_with_list.append(self.bg_images[i-1].get_width())
            self.tiles_list.append(math.ceil(width / self.bg_with_list[i]))


    def move(self, direction, max_width):

        for i in range(0,self.bg_num):
            self.speed_list.append(self.speed + (i + 1))
            self.x_list[i] = self.x_list[i] + (direction * self.speed_list[i])




