import pygame


class Player():


    def __init__(self, x, y, width, height, speed):
        self.walk_num = 9
        self.char_num = 6
        self.walkRight = []
        self.WalkRight_rect = []
        self.walkLeft = []
        self.walkLeft_rect = []
        self.char = []
        self.char_rect = []
        self.jump_distance = 50
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.topx_player = 100
        self.jump_y = []


        for i in range(0,self.walk_num):
            self.walkRight.append(pygame.image.load(f"assets/Characters/knight/walk/walk_knight_{i+1}.png"))
            self.walkRight[i] = pygame.transform.scale(self.walkRight[i], (width, height))
            self.WalkRight_rect.append(self.walkRight[i].get_rect())


            self.walkLeft.append(pygame.image.load(f"assets/Characters/knight/walk/walk_knight_{i+1}.png"))
            self.walkLeft[i] = pygame.transform.flip(self.walkLeft[i], 1, 0)
            self.walkLeft[i] = pygame.transform.scale(self.walkLeft[i], (width, height))
            self.walkLeft_rect.append(self.walkLeft[i].get_rect())


        for i in range(0,self.char_num):
            self.char.append(pygame.image.load(f"assets/Characters/knight/idle/idle_knight_{i+1}.png"))
            self.char[i] = pygame.transform.scale(self.char[i], (width, height))
            self.char_rect.append(self.char[i].get_rect())


        self.walkCount = 0
        self.isJump = False

        image = pygame.image.load('assets/Characters/knight/walk/walk_knight_1.png')
        #self.image = pygame.transform.flip(image, 1, 0)
        self.image = pygame.transform.scale(image, (width, height))




    def move(self, direction, max_width):

        #self.s += (direction * self.speed)
        if (self.x >= max_width + self.topx_player and direction > 0) or (self.x <= max_width - self.topx_player * 2 and direction < 0):
            return

        self.x += (direction * self.speed)

    def jump(self, direction, max_width):
        for up_down in range(0, self.jump_distance):
            self.jump_y.append(self.y-up_down)
        for down_up in range (0, self.jump_distance):
            self.jump_y.append((self.y-self.jump_distance)+down_up)



