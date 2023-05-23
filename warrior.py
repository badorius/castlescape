from settings import *
from sounds import *


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
        self.level = 0
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

    def reset(self, x, y, world):
        self.live = self.live_max
        self.timer = 6000
        self.rect.x = x
        self.rect.y = y
        self.world = world

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










