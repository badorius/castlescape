import pygame
import os


class Sprite(pygame.sprite.Sprite):
    def __init__(self, folderPath):
        super(Sprite, self).__init__()

        # Name of the folder in which all the
        # images are stored
        #folderPath = "Character_images_left"

        # Storing the folder location in a list
        self.myList = os.listdir(folderPath)
        self.images = []
        for imPath in self.myList:
            # Appending all the images in the array
            self.images.append(pygame.image.load(f'{folderPath}/{imPath}'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 150, 198)

    def update(self):

        # Increase the value of the index by 1
        # so that we can change the sprite images
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]