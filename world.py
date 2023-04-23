import pygame
from settings import *
from random import randint

class World():
    def __init__(self, data):
        self.tile_list = []
        self.scroll = 0
        self.speed = 1
        #load img
        dirt_img = pygame.image.load('assets/Tiles/floor_tile_2.png')
        grass_img = pygame.image.load('assets/Tiles/floor_tile_carpet_2.png')
        barrel_img = pygame.image.load('assets/Decorations/barrel.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()

                    img_rect.x = col_count * tile_size
                    print(img_rect.x)
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(barrel_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1


    def draw(self):
        speed = 1
        for tile in self.tile_list:
            win.blit(tile[0], tile[1])

    def draw_ground(self):
        floor_rnd = randint(1, 10)
        for z in range(1000):

            for x in range(1, 5):
                win.blit(self.floor1[x - 1], (
                x + z * (self.floor1[x - 1].get_width()) - self.scroll * 2.2, window_height - self.floor1[x - 1].get_height()))


    def drawgrid(self):
        for line in range(0, 400):
            pygame.draw.line(win, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
            pygame.draw.line(win, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))