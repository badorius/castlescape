import pygame


class Player():


    def __init__(self, x, y, width, height, speed):
        self.walk_num = 9
        self.char_num = 6
        self.walkRight = []
        self.walkLeft = []
        self.char = []

        for i in range(0,self.walk_num):
            self.walkRight.append(pygame.image.load(f"assets/Characters/knight/walk/walk_knight_{i+1}.png"))
            self.walkRight[i] = pygame.transform.scale(self.walkRight[i], (width, height))

            self.walkLeft.append(pygame.image.load(f"assets/Characters/knight/walk/walk_knight_{i+1}.png"))
            self.walkLeft[i] = pygame.transform.flip(self.walkLeft[i], 1, 0)
            self.walkLeft[i] = pygame.transform.scale(self.walkLeft[i], (width, height))


        for i in range(0,self.char_num):
            self.char.append(pygame.image.load(f"assets/Characters/knight/idle/idle_knight_{i+1}.png"))
            self.char[i] = pygame.transform.scale(self.char[i], (width, height))


        self.walkCount = 0
        self.isJump = False

        image = pygame.image.load('assets/Characters/knight/walk/walk_knight_1.png')
        #self.image = pygame.transform.flip(image, 1, 0)
        self.image = pygame.transform.scale(image, (width, height))



        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed



    def move(self, direction, max_width):

        #self.s += (direction * self.speed)
        if (self.x >= max_width - self.width and direction > 0) or (self.x <= 0 and direction < 0):
            return

        self.x += (direction * self.speed)

    def jump(self, direction, max_width):
        if (self.y >= max_width - self.width and direction > 0) or (self.y <= 0 and direction < 0):
            return

        self.y += (direction * self.speed)




