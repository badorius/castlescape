import pygame
from settings import *
from random import randint

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/Characters/enemy/burning-ghoul-3.png')
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 5
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 10
        if abs(self.move_counter) > 300:
            self.move_direction *= -1
            self.move_counter *= -1
