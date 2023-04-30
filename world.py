import pygame
from settings import *
from obstacle import *
from platform import *
from random import randint

class World():
    def __init__(self, data, obstacle_group, platform_group):
        self.tile_list = []
        self.floor1 = []
        self.scroll = 0
        self.speed = 1
        self.collide = "none"

        #Load floor1 images
        for z in range(1, 5):
            self.floor1.append(pygame.image.load(f"assets/Tiles/floor_tile_{z}.png"))

        floor_tile_1 = pygame.image.load('assets/Tiles/floor_tile_2.png')
        barrel_img_2 = pygame.image.load('assets/Decorations/barrel.png')
        potion_1_img_4 = pygame.image.load('assets/Decorations/potion_1.png')
        brick1_img_5 = pygame.image.load('assets/Tiles/brick_1.png')
        spikes_img_6 = pygame.image.load('assets/Tiles/spikes.png')

        # Add image to tile list map with rect
        def to_tile_list(tile_img, tile,  col, row):
            img = pygame.transform.scale(tile_img, (tile_size, tile_size))
            img_rect = img.get_rect()
            img_rect.x = col * tile_size
            img_rect.y = row * tile_size
            tile = (img, img_rect)
            self.tile_list.append(tile)


        # Double for to full tile map with row and columns.
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    to_tile_list(floor_tile_1, tile, col_count, row_count)
                if tile == 2:
                    to_tile_list(barrel_img_2, tile, col_count, row_count)
                if tile == 3:
                    obstacle = Obstacle(col_count * tile_size, row_count * tile_size - 150)
                    obstacle_group.add(obstacle)
                if tile == 4:
                    to_tile_list(potion_1_img_4, tile, col_count, row_count)
                if tile == 5:
                    platform = Platform(col_count * tile_size, row_count * tile_size - 150)
                    platform_group.add(platform)
                if tile == 6:
                    to_tile_list(spikes_img_6, tile, col_count, row_count)
                col_count += 1
            row_count += 1


    def draw(self):
        for tile in self.tile_list:
            win.blit(tile[0], tile[1])
            #pygame.draw.rect(win, (255, 255, 255), tile[1], 2)

    def move(self, direction):
        for z in range(len(self.tile_list)):
            tile = self.tile_list[z]
            img = tile[0]
            img_rect = tile[1]
            #pygame.draw.rect(win, (255, 255, 255), img_rect, 2)
            img_rect.x -= direction


    def drawgrid(self):
        for line in range(0, 400):
            pygame.draw.line(win, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
            pygame.draw.line(win, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))