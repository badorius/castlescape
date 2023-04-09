import pygame
from gameObject import GameObject

class Player(GameObject):


    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)

        self.speed = speed
        self.walkRight = [pygame.image.load('assets/Characters/knight/walk/walk_knight_1.png'),
                     pygame.image.load('assets/Characters/knight/walk/walk_knight_2.png'),
                     pygame.image.load('assets/Characters/knight/walk/walk_knight_3.png'),
                     pygame.image.load('assets/Characters/knight/walk/walk_knight_4.png'),
                     pygame.image.load('assets/Characters/knight/walk/walk_knight_5.png'),
                     pygame.image.load('assets/Characters/knight/walk/walk_knight_6.png'),
                     pygame.image.load('assets/Characters/knight/walk/walk_knight_7.png'),
                     pygame.image.load('assets/Characters/knight/walk/walk_knight_8.png'),
                     pygame.image.load('assets/Characters/knight/walk/walk_knight_9.png')]

        self.walkLeft = [pygame.image.load('assets/Characters/knight/walk/walk_knight_1.png'),
                    pygame.image.load('assets/Characters/knight/walk/walk_knight_2.png'),
                    pygame.image.load('assets/Characters/knight/walk/walk_knight_3.png'),
                    pygame.image.load('assets/Characters/knight/walk/walk_knight_4.png'),
                    pygame.image.load('assets/Characters/knight/walk/walk_knight_5.png'),
                    pygame.image.load('assets/Characters/knight/walk/walk_knight_6.png'),
                    pygame.image.load('assets/Characters/knight/walk/walk_knight_7.png'),
                    pygame.image.load('assets/Characters/knight/walk/walk_knight_8.png'),
                    pygame.image.load('assets/Characters/knight/walk/walk_knight_9.png')]

        self.char = [pygame.image.load('assets/Characters/knight/idle/idle_knight_1.png'),
                pygame.image.load('assets/Characters/knight/idle/idle_knight_2.png'),
                pygame.image.load('assets/Characters/knight/idle/idle_knight_3.png'),
                pygame.image.load('assets/Characters/knight/idle/idle_knight_4.png'),
                pygame.image.load('assets/Characters/knight/idle/idle_knight_5.png'),
                pygame.image.load('assets/Characters/knight/idle/idle_knight_6.png')]

        self.walkCount = 0
        self.isJump = False


    def move(self, direction, max_width):

        #self.s += (direction * self.speed)
        if (self.x >= max_width - self.width and direction > 0) or (self.x <= 0 and direction < 0):
            return

        self.x += (direction * self.speed)




