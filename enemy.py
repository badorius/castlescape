import pygame


class Enemy():


    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.speed = speed
        image = pygame.image.load('assets/enemy.png')
        self.image = pygame.transform.scale(image, (width, height))
    def move(self, max_width):
        if self.x <= 0:
            self.speed = abs(self.speed)
        elif self.x >= max_width - self.width:
            self.speed = -self.speed

        self.x += self.speed
        


