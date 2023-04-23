import pygame
from settings import *
from random import randint


class Warrior():

    def __init__(self):

        self.isJump = False
        self.left = False
        self.right = False
        self.attack = False
        self.jumpCount = 10
        self.attackCount = 11
        self.width = 100
        self.height = 100
        self.x = 400
        self.y = 700
        self.face = "Right"
        self.walkCount = 0
        self.idle = 0
        self.idle_floor = 0
        self.hurt = 0
        self.hurt_floor = 0
        self.walkLeft = []
        self.walkRight = []
        self.char_jump = []
        self.char = []
        self.char_hurt = []
        self.char_attack = []
        self.floor1 = []


        #Sprite Run Left and Right
        for z in range(1, 9):
            self.walkRight.append(pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Run/Warrior_Run_{z}.png"))
            self.walkLeft.append(pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Run/Warrior_Run_{z}.png"))
            self.walkRight[z - 1] = pygame.transform.scale(self.walkRight[z - 1], (self.width, self.height))
            self.walkLeft[z - 1] = pygame.transform.scale(self.walkLeft[z - 1], (self.width, self.height))
            self.walkLeft[z - 1] = pygame.transform.flip(self.walkLeft[z - 1], True, False)

        #Sprite idle
        for z in range(1, 7):
            self.char.append(pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/idle/Warrior_Idle_{z}.png"))
            self.char[z - 1] = pygame.transform.scale(self.char[z - 1], (self.width, self.height))


        #Sprite jump
        for z in range(1, 4):
            self.char_jump.append(pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Jump/Warrior_Jump_{z}.png"))
            self.char_jump[z - 1] = pygame.transform.scale(self.char_jump[z - 1], (self.width, self.height))

        #Sprite hurt
        for z in range(1,5):
            self.char_hurt.append(pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Hurt-Effect/Warrior_hurt_{z}.png"))
            self.char_hurt[z - 1] = pygame.transform.scale(self.char_hurt[z - 1], (self.width, self.height))


        #Sprite atack
        for z in range(1,13):
            self.char_attack.append(pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Attack/Warrior_Attack_{z}.png"))
            self.char_attack[z - 1] = pygame.transform.scale(self.char_attack[z - 1], (self.width, self.height))

        self.char_rect = self.char[0].get_rect()


    def reverse_warrior(self):
        #Sprite idle
        for z in range(1, 7):
            self.char[z - 1] = pygame.transform.flip(self.char[z - 1], True, False)

        #Sprite jump
        for z in range(1, 4):
            self.char_jump[z - 1] = pygame.transform.flip(self.char_jump[z - 1], True, False)

        #Sprite hurt
        for z in range(1,5):
            self.char_hurt[z - 1] = pygame.transform.flip(self.char_hurt[z - 1], True, False)

        #Sprite atack
        for z in range(1,13):
            self.char_attack[z - 1] = pygame.transform.flip(self.char_attack[z - 1], True, False)


    def move(self):
        self.char_rect.x = self.x
        self.char_rect.y = self.y
        if self.face == "Right":
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
        elif self.face == "Left":
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))


