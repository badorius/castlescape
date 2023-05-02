import pygame
from settings import *
from random import randint


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size = tile_size * 1
        self.image = pygame.image.load('assets/Characters/enemy/burning-ghoul-3.png')
        self.image = pygame.transform.scale(self.image, (self.size * 2, self.size * 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - tile_size - 25
        self.move_direction = 5
        self.move_counter = 0
        self.direction = 1


    def update(self, x):
        self.rect.x += self.move_direction
        self.rect.x -= x
        self.move_counter += 10
        if abs(self.move_counter) > 300:
            self.move_direction *= -1
            if self.move_direction < 0:
                self.direction = -1
                self.image = pygame.image.load('assets/Characters/enemy/burning-ghoul-3.png')
                self.image = pygame.transform.scale(self.image, (self.size * 2, self.size * 2))
                pygame.transform.flip(self.image, True, False)
                #print(self.direction)
            self.move_counter *= -1
            if self.move_direction > 1:
                self.direction = 1
                self.image = pygame.image.load('assets/Characters/enemy/burning-ghoul-3.png')
                self.image = pygame.transform.scale(self.image, (self.size * 2, self.size * 2))
                pygame.transform.flip(self.image, True, False)

        #print(self.move_counter)

