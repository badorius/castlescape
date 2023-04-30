import pygame
from settings import *
from random import randint
from sounds import *
from sprite import *
from math import *
from sounds import *
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
        self.live_max = 450
        self.live = 450

        self.index_run = 0
        self.index_idle = 0
        self.index_attack = 0
        self.index_hurt = 0
        self.index_jump = 0

        self.counter = 0
        self.jump_counter = 0
        self.dx = 0
        self.dy = 0
        self.size_width = 100
        self.size_height = 100
        self.collide_enemy = False
        self.collide_obstacle = False
        self.collide_platform = False
        self.collide_spikes = False
        self.in_air = True



        #Sprite RUN
        for num in range(1, 9):
            img_right = pygame.image.load(f'assets/Characters/Warrior/IndividualSprite/Run/Warrior_Run_{num}.png')
            img_right = pygame.transform.scale(img_right, (self.size_width, self.size_height))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        #Sprite idle
        for num in range(1, 7):
            img_idle_right = pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/idle/Warrior_Idle_{num}.png")
            img_idle_right = pygame.transform.scale(img_idle_right, (self.size_width, self.size_height))
            img_idle_left = pygame.transform.flip(img_idle_right, True, False)
            self.images_idle_right.append(img_idle_right)
            self.images_idle_left.append(img_idle_left)

        #Sprite jump
        for num in range(1, 4):
            img_jump_right = pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Jump/Warrior_Jump_{num}.png")
            img_jump_right = pygame.transform.scale(img_jump_right, (self.size_width, self.size_height))
            img_jump_left = pygame.transform.flip(img_jump_right, True, False)
            self.images_jump_right.append(img_jump_right)
            self.images_jump_left.append(img_jump_left)

        #Sprite hurt
        for num in range(1,5):
            img_hurt_right = pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Hurt-Effect/Warrior_hurt_{num}.png")
            img_hurt_right = pygame.transform.scale(img_hurt_right, (self.size_width, self.size_height))
            img_hurt_left = pygame.transform.flip(img_hurt_right, True, False)
            self.images_hurt_right.append(img_hurt_right)
            self.images_hurt_left.append(img_hurt_left)

        #Sprite atack
        for num in range(1,13):
            img_attack_right = pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Attack/Warrior_Attack_{num}.png")
            img_attack_right = pygame.transform.scale(img_attack_right, (self.size_width, self.size_height))
            img_attack_left = pygame.transform.flip(img_attack_right, True, False)
            self.images_attack_right.append(img_attack_right)
            self.images_attack_left.append(img_attack_left)

        self.image = self.images_idle_right[self.index_run]
        self.rect = self.image.get_rect()
        self.rect.inflate(70, 100 )
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

    def update(self, world, obstacle_group, platform_group, potion_group, spikes_group):
        self.dx = 0
        self.dy = 0
        walk_cooldown = 5
        col_thresh = 20

        # handle animation
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index_run += 1
            self.index_attack += 1
            self.index_idle += 1

            #RUN
            if self.right or self.left:
                if self.index_run >= len(self.images_right):
                    self.index_run = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index_run]
                if self.direction == -1:
                    self.image = self.images_left[self.index_run]

            #ATTACK
            if self.attack:
                if self.index_attack >= len(self.images_attack_right):
                    self.index_attack = 0
                if self.direction == 1:
                    self.image = self.images_attack_right[self.index_attack]
                if self.direction == -1:
                    self.image = self.images_attack_left[self.index_attack]

            #JUMP
            if self.jumped:
                if self.jumped >= len(self.images_jump_right):
                    self.index_jump = 0
                if self.direction == 1:
                    self.image = self.images_jump_right[self.index_jump]
                if self.direction == -1:
                    self.image = self.images_jump_left[self.index_jump]

            #IDLE
            if self.idle:
                if self.index_idle >= len(self.images_idle_right):
                    self.index_idle = 0
                if self.direction == 1:
                    self.image = self.images_idle_right[self.index_idle]
                if self.direction == -1:
                    self.image = self.images_idle_left[self.index_idle]

            # Collide obstacle
            if self.collide_obstacle or self.collide_spikes:
                if self.index_hurt >= len(self.images_hurt_right):
                    self.index_hurt = 0
                if self.direction == 1:
                    self.image = self.images_hurt_right[self.index_hurt]
                if self.direction == -1:
                    self.image = self.images_hurt_left[self.index_hurt]


        # add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        self.dy += self.vel_y

        # check for collision
        self.in_air = True
        for tile in world.tile_list:
            # check for collision in x direction
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0

            # check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                # check if below the ground i.e. jumping
                if self.vel_y < 0:
                    self.dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                # check if above the ground i.e. falling
                elif self.vel_y >= 0:
                    self.dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.in_air = True

            # Check collide obstacle
            if pygame.sprite.spritecollide(self, obstacle_group, False):
                self.collide_obstacle = True
                pygame.mixer.Sound.play(hurt)

                self.live -= 0.1
                if self.direction == 1:
                    self.dx -= 0.1
                if self.direction == -1:
                    self.dx += 0.1
            else:
                self.collide_obstacle = False

            # Check spikes collide
            if pygame.sprite.spritecollide(self, spikes_group, False):
                self.collide_spikes = True
                pygame.mixer.Sound.play(hurt)
                self.live -= 0.1
                if self.direction == 1:
                    self.dy -= 0.1
                if self.direction == -1:
                    self.dy += 0.1
            else:
                self.collide_spikes = False

            # check for collision with platforms
            for platform in platform_group:
                # collision in the x direction
                if platform.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                    self.dx = 0
                # collision in the y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                    # check if below platform
                    if abs((self.rect.top + self.dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        self.dy = platform.rect.bottom - self.rect.top
                    # check if above platform
                    elif abs((self.rect.bottom + self.dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top - 1
                        self.in_air = False
                        self.dy = 0
                    # move sideways with the platform
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction

            # FALL DOWN
            if self.rect.y > window_height - tile_size * 2:
                pygame.mixer.Sound.play(hurt)
                self.collide_obstacle = True
                self.live -= 0.1
            else:
                self.collide_obstacle = False

            # Collide Potion
            if pygame.sprite.spritecollide(self, potion_group, False):
                if self.live < self.live_max - 10:
                    pygame.mixer.Sound.play(get_potion)
                    self.live += 10
                else:
                    self.live = self.live_max
                    pygame.mixer.Sound.play(get_potion)


            

        # update player coordinates
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.dy = 0

        # draw player onto screen
        win.blit(self.image, self.rect)
        #pygame.draw.rect(win, (255, 255, 255), self.rect, 2)


