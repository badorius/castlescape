import pygame
from gameObject import GameObject


class Background(GameObject):

    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)

        self.speed = speed
        self.background1 = GameObject(0, 0, self.width, self.height, 'assets/Background/layer_1.png')
        self.background2 = GameObject(0, 0, self.width, self.height, 'assets/Background/layer_2.png')
        self.background3 = GameObject(0, 0, self.width, self.height, 'assets/Background/layer_3.png')

    def move(self, direction, max_width):
        # self.s += (direction * self.speed)
        if (self.x >= max_width - self.width and direction > 0) or (self.x <= 0 and direction < 0):
            return

        self.x += (direction * self.speed)
