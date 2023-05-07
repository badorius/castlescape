import pygame.transform

from settings import *
from sounds import *
import spritesheet

class Warrior():
    def __init__(self, x, y, world):
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
        self.direction = 1
        self.index_run = 0
        self.index_idle = 0
        self.index_attack = 0
        self.index_hurt = 0
        self.index_jump = 0
        self.world = world
        self.counter = 0
        self.jump_counter = 0
        self.dx = 0
        self.dy = 0
        self.size_width = 44
        self.size_height = 64
        self.offset = 10
        #self.size_width = 100
        #self.size_height = 100
        self.collide_enemy = False
        self.collide_obstacle = False
        self.collide_platform = False
        self.collide_spikes = False
        self.in_air = True
        self.level_completed = False
        self.collide_right = False
        self.collide_left = False
        self.timer = 6000
        self.score = 0
        BLACK = (0, 0, 0)

        #Sprite RUN
        for num in range(1, 9):
            img_right = pygame.image.load(f'assets/Characters/Warrior/IndividualSprite/Run/Warrior_Run_{num}.png').convert_alpha()
            img_right = pygame.transform.scale_by(img_right, (2))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        #Sprite idle
        for num in range(1, 7):
            img_idle_right = pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/idle/Warrior_Idle_{num}.png").convert_alpha()
            img_idle_right = pygame.transform.scale_by(img_idle_right, (2))
            img_idle_left = pygame.transform.flip(img_idle_right, True, False)
            self.images_idle_right.append(img_idle_right)
            self.images_idle_left.append(img_idle_left)

        #Sprite jump
        for num in range(1, 4):
            img_jump_right = pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Jump/Warrior_Jump_{num}.png").convert_alpha()
            img_jump_right = pygame.transform.scale_by(img_jump_right, (2))
            img_jump_left = pygame.transform.flip(img_jump_right, True, False)
            self.images_jump_right.append(img_jump_right)
            self.images_jump_left.append(img_jump_left)

        #Sprite hurt
        for num in range(1,5):
            img_hurt_right = pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Hurt-Effect/Warrior_hurt_{num}.png").convert_alpha()
            img_hurt_right = pygame.transform.scale_by(img_hurt_right, (2))
            img_hurt_left = pygame.transform.flip(img_hurt_right, True, False)
            self.images_hurt_right.append(img_hurt_right)
            self.images_hurt_left.append(img_hurt_left)

        #Sprite atack
        for num in range(1,13):
            img_attack_right = pygame.image.load(f"assets/Characters/Warrior/IndividualSprite/Attack/Warrior_Attack_{num}.png").convert_alpha()
            img_attack_right = pygame.transform.scale_by(img_attack_right, (2))
            img_attack_left = pygame.transform.flip(img_attack_right, True, False)
            self.images_attack_right.append(img_attack_right)
            self.images_attack_left.append(img_attack_left)

        self.image = self.images_idle_right[self.index_run].convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.width = self.image.get_width()/3
        self.rect.height = self.image.get_height()/1.2
        self.rect.x = x
        self.rect.y = y
        self.left = False
        self.right = False
        self.attack = False
        self.jumped = False
        self.idle = True
        self.vel_y = 0
        self.direction = 0

    def update(self):
        walk_cooldown = 5
        self.timer -= 1
        self.timer = int(self.timer)

        # handle animation
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index_run += 1
            self.index_attack += 1
            self.index_idle += 1
            #self.index_jump += 1

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

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.dy = 0

        # update player coordinates
        self.rect.x += self.dx
        self.rect.y += self.dy



        # draw player onto screen -30 and - 20 offset to put image on to rect
        if self.direction == 1:
            win.blit(self.image, (self.rect.x - 30, self.rect.y - 20, self.rect.width, self.rect.height))
        if self.direction == -1:
            win.blit(self.image, (self.rect.x - 50, self.rect.y - 20, self.rect.width, self.rect.height))
        #pygame.draw.rect(win, (255, 255, 255), self.rect, 2)



    def check_collide(self):
        self.in_air = True
        col_thresh = 20
        self.dx = 0
        self.dy = 0
        # check for collision
        for tile in self.world.tile_list:
            # check for collision in x direction
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.rect.width, self.rect.height):
                self.dx = 0
            # check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.rect.width, self.rect.height):
                # check if below the ground i.e. jumping
                if self.vel_y < - 15:
                    self.dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                    print("ah")
                # check if above the ground i.e. falling
                elif self.vel_y >= 0:
                    self.dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.in_air = False


            # Check collide obstacle
            if pygame.sprite.spritecollide(self, self.world.obstacle_group, False):
                self.collide_obstacle = True
                pygame.mixer.Sound.play(hurt)
                self.live -= 0.1
                if self.direction == 1:
                    self.dx -= 0.1
                if self.direction == -1:
                    self.dx += 0.1
            else:
                self.collide_obstacle = False

            # Check collide enemy
            if self.attack == True:
                if pygame.sprite.spritecollide(self, self.world.enemy_group, True):
                    self.collide_enemy = False
                    self.score += 1
            else:
                if pygame.sprite.spritecollide(self, self.world.enemy_group, False):
                    self.collide_enemy = True
                    pygame.mixer.Sound.play(hurt)
                    self.live -= 0.1
                    if self.direction == 1:
                        self.dx -= 0.1
                    if self.direction == -1:
                        self.dx += 0.1


            # Check spikes collide
            if pygame.sprite.spritecollide(self, self.world.spikes_group, False):
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
            for platform in self.world.platform_group:
                # collision in the x direction
                if platform.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.rect.width, self.rect.height):
                    self.dx = 0
                # collision in the y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.rect.width, self.rect.height):
                    # check if below platform
                    if abs((self.rect.top + self.dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        self.dy = platform.rect.bottom - self.rect.top
                    # check if above platform
                    elif abs((self.rect.bottom + self.dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top
                        self.in_air = False
                        self.dy = 0
                        self.counter += 1

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
            if pygame.sprite.spritecollide(self, self.world.potion_group, True):
                if self.live < self.live_max - 50:
                    pygame.mixer.Sound.play(get_potion)
                    self.live += 50
                else:
                    self.live = self.live_max
                    pygame.mixer.Sound.play(get_potion)

            # Collide Door
            if pygame.sprite.spritecollide(self, self.world.door_group, False):
                self.level_completed = True


    def keypress(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
            pygame.mixer.Sound.play(jump)
            self.vel_y = - 15
            self.jumped = True
            self.left = False
            self.right = False
            self.idle = False
            self.counter += 1
        if key[pygame.K_SPACE] == False:
            self.jumped = False

        if key[pygame.K_LCTRL]:
            pygame.mixer.Sound.play(attack_sound)
            self.attack = True
            self.left = False
            self.right = False
            self.idle = False
            for z in (0, len(self.images_attack_right)):
                self.counter += 1


        if key[pygame.K_LEFT]:
            self.dx -= vel
            self.left = True
            self.right = False
            self.idle = False
            self.counter += 1
            self.direction = -1

        if key[pygame.K_RIGHT]:
            self.dx += vel
            self.left = False
            self.right = True
            self.idle = False
            self.counter += 1
            self.direction = 1

        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and key[pygame.K_LCTRL] == False:
            self.idle = True
            self.left = False
            self.right = False
            self.attack = False
            self.counter += 1
            # ingrid.index_run = 1

        self.check_collide()
        self.update()




