import pygame
from settings import *
from random import randint


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size = tile_size * 1
        self.image = pygame.image.load('assets/Tiles/brick_1.png')
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 5
        self.move_counter = 0


    def update(self, x):
        self.rect.y += self.move_direction
        self.rect.x -= x
        self.move_counter += 10
        if abs(self.move_counter) > 300:
            self.move_direction *= -1
            self.move_counter *= -1
