import pygame


class Background():

    def __init__(self, x, y, width, height, speed):

        self.x1 = x
        self.x2 = x
        self.x3 = x

        self.y1 = y
        self.y2 = y
        self.y3 = y


        self.width = width
        self.height = height
        self.bg_image1 = 'assets/Background/layer_1.png'
        self.bg_image2 = 'assets/Background/layer_2.png'
        self.bg_image3 = 'assets/Background/layer_3.png'
        self.bg_images = [self.bg_image1, self.bg_image2, self.bg_image3]

        self.image1 = pygame.image.load(self.bg_image1)
        self.image2 = pygame.image.load(self.bg_image2)
        self.image3 = pygame.image.load(self.bg_image3)

        self.image1 = pygame.transform.scale(self.image1, (width, height))
        self.image2 = pygame.transform.scale(self.image2, (width, height))
        self.image3 = pygame.transform.scale(self.image3, (width, height))

        self.width = width
        self.height = height
        self.speed = speed * 2



    def move(self, direction, max_width):

        self.speed1 = self.speed + 1
        self.speed2 = self.speed + 2
        self.speed3 = self.speed + 3
        self.x1 += (direction * self.speed1)
        self.x2 += (direction * self.speed2)
        self.x3 += (direction * self.speed3)
