import pygame
from settings import *
from random import randint
from sounds import *
from sprite import *
from math import *
class Warrior():

    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.images_idle_right = []
        self.images_idle_left = []
        self.images_jump_right = []
        self.images_jump_left = []
        self.images_hurt_right = []
        self.images_hurt_left = []
        self.images_attack_right = []
        self.images_attack_left = []
        self.index_run = 0
        self.index_idle = 0
        self.counter = 0

        #Sprite RUN
        for num in range(1, 9):
            img_right = pygame.image.load(f'assets/Characters/Warrior/IndividualSprite/Run/Warrior_Run_{num}.png')
            img_right = pygame.transform.scale(img_right, (100, 100))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        #Sprite idle
        for num in range(1, 7):
            img_idle_right = pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/idle/Warrior_Idle_{num}.png")
            img_idle_right = pygame.transform.scale(img_idle_right, (100, 100))
            img_idle_left = pygame.transform.flip(img_idle_right, True, False)
            self.images_idle_right.append(img_idle_right)
            self.images_idle_left.append(img_idle_left)

        #Sprite jump
        for num in range(1, 4):
            img_jump_right = pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Jump/Warrior_Jump_{num}.png")
            img_jump_right = pygame.transform.scale(img_jump_right, (100, 100))
            img_jump_left = pygame.transform.flip(img_jump_right, True, False)
            self.images_jump_right.append(img_jump_right)
            self.images_jump_left.append(img_jump_left)

        #Sprite hurt
        for num in range(1,5):
            img_hurt_right = pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Hurt-Effect/Warrior_hurt_{num}.png")
            img_hurt_right = pygame.transform.scale(img_hurt_right, (100, 100))
            img_hurt_left = pygame.transform.flip(img_hurt_right, True, False)
            self.images_hurt_right.append(img_hurt_right)
            self.images_hurt_left.append(img_hurt_left)

        #Sprite atack
        for num in range(1,13):
            img_attack_right = pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Attack/Warrior_Attack_{num}.png")
            img_attack_right = pygame.transform.scale(img_attack_right, (100, 100))
            img_attack_left = pygame.transform.flip(img_attack_right, True, False)
            self.images_attack_right.append(img_attack_right)
            self.images_attack_left.append(img_attack_left)

        self.image = self.images_right[self.index_run]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left = False
        self.right = False
        self.attack = False
        self.jumped = False
        self.idle = True
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.direction = 0

    def update(self, world):
        dx = 0
        dy = 0
        walk_cooldown = 5

        # get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            pygame.mixer.Sound.play(ouch)
            self.vel_y = -15
            self.jumped = True
            self.idle = False

        if key[pygame.K_SPACE] == False:
            self.jumped = False

        if key[pygame.K_LEFT]:
            self.left = True
            self.right = False
            self.idle = False
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_RIGHT]:
            self.left = False
            self.right = True
            self.idle = False
            dx += 5
            self.counter += 1
            self.direction = 1

        if key[pygame.K_LCTRL]:
            self.attack = True
            self.idle = False
            pygame.mixer.Sound.play(ouch)


        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.left = False
            self.right = False
            self.idle = True
            self.attack = False
            self.counter = 0
            self.index_run = 0


        # handle animation
        if self.counter > walk_cooldown:

            self.counter = 0
            # RUN
            self.index_run += 1
            if self.index_run >= len(self.images_right):
                self.index_run = 0
            if self.direction == 1:
                self.image = self.images_right[self.index_run]
                if self.attack:
                    self.image = self.images_attack_right[self.index_run]
            if self.direction == -1:
                self.image = self.images_left[self.index_run]
                if self.attack:
                    self.image = self.images_attack_left[self.index_run]


        # IDLE
        if not (self.right or self.left):
            self.index_idle += 1
            if self.index_idle >= len(self.images_idle_right):
                self.index_idle = 0
            if self.direction == 1:
                self.image = self.images_idle_right[self.index_idle]
                if self.attack:
                    self.image = self.images_attack_left[self.index_run]
            if self.direction == -1:
                self.image = self.images_idle_left[self.index_idle]
                if self.attack:
                    self.image = self.images_attack_left[self.index_run]


        # add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # check for collision
        for tile in world.tile_list:
            # check for collision in x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            # check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground i.e. jumping
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                # check if above the ground i.e. falling
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0

        # update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0

        # draw player onto screen
        win.blit(self.image, self.rect)
        #pygame.draw.rect(win, (255, 255, 255), self.rect, 2)


