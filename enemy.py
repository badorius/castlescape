import pygame
from settings import *
from random import randint


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size = tile_size * 1
        self.images_right = []
        self.images_left = []
        self.counter = 0


        #Sprite RUN
        for num in range(1, 9):
            self.img_right = pygame.image.load(f'assets/Characters/enemy/Bringer-Of-Death/Individual Sprite/Walk/Bringer-of-Death_Walk_{num}.png').convert_alpha()
            self.img_right = pygame.transform.scale_by(self.img_right, (4))
            self.img_left = pygame.transform.flip(self.img_right, True, False)
            self.images_right.append(self.img_right)
            self.images_left.append(self.img_left)


        self.image = self.images_right [self.counter]
        self.image = pygame.transform.scale(self.image, (self.size * 4, self.size * 4))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - tile_size - 100
        self.move_direction = 5
        self.move_counter = 0
        self.direction = 1
        self.live = 1

    def update(self, x):

        self.move_counter += 10
        if self.counter >= len(self.images_right):
            self.counter = 0
            print("reset counter")

        if self.live > 1:
            self.image = self.images_right[self.counter]
            self.image = pygame.transform.scale(self.image, (self.size * 4, self.size * 4))
            self.counter += 1
        if abs(self.move_counter) > 300:
            self.move_direction *= -1
            if self.move_direction < 0:
                self.direction = -1
                self.image = self.images_right[self.counter]
                self.image = pygame.transform.scale(self.image, (self.size * 4, self.size * 4))
                #self.image = pygame.transform.flip(self.image, True, False)
                #print(self.direction)
                self.counter += 1
                print(self.counter)

            self.move_counter *= -1
            if self.move_direction > 1:
                self.direction = 1
                self.image = self.images_right[self.counter]
                self.image = self.image = pygame.transform.scale(self.image, (self.size * 4, self.size * 4))
                self.image = pygame.transform.flip(self.image, True, False)
                self.counter += 1
                print(self.counter)

        self.rect.x += self.move_direction
        self.rect.x -= x

        #self.counter += 1
        #print(self.move_counter)

