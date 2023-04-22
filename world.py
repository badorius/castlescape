import pygame
from settings import *

class World():
    def __init__(self, data):
        self.tile_list = []
        self.scroll = 0
        self.speed = 1
        #load img
        dirt_img = pygame.image.load('assets/Tiles/floor_tile_2.png')
        grass_img = pygame.image.load('assets/Tiles/floor_tile_carpet_2.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * tile_size) - (self.scroll * self.speed)
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size - (self.scroll * self.speed)
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1


    def draw(self):
        speed = 1
        for tile in self.tile_list:
            win.blit(tile[0], tile[1])

    def drawgrid(self):
        for line in range(0, 400):
            pygame.draw.line(win, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
            pygame.draw.line(win, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))