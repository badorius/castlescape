import pygame
from settings import *
from random import randint


class Enemy():

    def __init__(self):

        self.idle = 0
        self.idle_floor = 0
        self.isJump = False
        self.jumpCount = 10
        self.width = 100
        self.height = 100
        self.x = 1000
        self.y = 670
        self.left = False
        self.right = False
        self.walkCount = 0
        self.idle = 0
        self.idle_floor = 0
        self.face = "Right"

        self.walkLeft = []
        self.walkRight = []
        self.char_jump = []
        self.char = []
        self.floor1 = []

        for z in range(1, 7):
            self.walkRight.append(pygame.image.load(f"assets/Characters/skeleton-rise-clothed/skeleton-rise-clothed-{z}.png"))
            self.walkRight[z - 1] = pygame.transform.scale(self.walkRight[z - 1], (self.width, self.height))

        for z in range(1, 7):
            self.walkLeft.append(pygame.image.load(f"assets/Characters/skeleton-rise-clothed/skeleton-rise-clothed-{z}.png"))
            self.walkLeft[z - 1] = pygame.transform.scale(self.walkLeft[z - 1], (self.width, self.height))
            self.walkLeft[z - 1] = pygame.transform.flip(self.walkLeft[z - 1], True, False)

        for z in range(1, 7):
            self.char.append(pygame.image.load(f"assets/Characters/skeleton-rise-clothed/skeleton-rise-clothed-{z}.png"))
            self.char[z - 1] = pygame.transform.scale(self.char[z - 1], (self.width, self.height))

        for z in range(1, 7):
            self.char_jump.append(pygame.image.load(f"assets/Characters/skeleton-rise-clothed/skeleton-rise-clothed-{z}.png"))
            self.char_jump[z - 1] = pygame.transform.scale(self.char_jump[z - 1], (self.width, self.height))

        self.enemy_rect = self.char[0].get_rect()


    def reverse(self):
        #Sprite idle
        for z in range(1, 7):
            self.walkRight[z - 1] = pygame.transform.flip(self.walkRight[z - 1], True, False)

        #Sprite idle
        for z in range(1, 7):
            self.walkLeft[z - 1] = pygame.transform.flip(self.walkLeft[z - 1], True, False)

        #Sprite jump
        for z in range(1, 4):
            self.char[z - 1] = pygame.transform.flip(self.char[z - 1], True, False)

        #Sprite hurt
        for z in range(1,5):
            self.char_jump[z - 1] = pygame.transform.flip(self.char_jump[z - 1], True, False)


    def draw(self):
        print(self.enemy_rect)

    def move(self):
        self.enemy_rect.x = self.x
        self.enemy_rect.y = self.y
        win.blit(self.char[self.idle_floor], (self.x, self.y))