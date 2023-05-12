import pygame
from settings import *
from objects import *
from enemy import *

from random import randint

class World1():
    def __init__(self, data):
        self.tile_list = []
        self.floor1 = []
        self.speed = 1
        self.collide = "none"
        self.obstacle_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        self.potion_group = pygame.sprite.Group()
        self.door_group = pygame.sprite.Group()
        self.spikes_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()

        #Load floor1 images
        for z in range(1, 5):
            self.floor1.append(pygame.image.load(f"assets/Tiles/floor_tile_{z}.png"))


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
                    to_tile_list(floor_tile_2, tile, col_count, row_count)
                if tile == 3:
                    to_tile_list(floor_tile_3, tile, col_count, row_count)
                if tile == 4:
                    to_tile_list(floor_tile_4, tile, col_count, row_count)
                if tile == 5:
                    to_tile_list(barrel_img_2, tile, col_count, row_count)
                if tile == 6:
                    obstacle = Obstacle(col_count * tile_size, row_count * tile_size - 150)
                    self.obstacle_group.add(obstacle)
                if tile == 7:
                    potion = Potion(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                    self.potion_group.add(potion)
                if tile == 8:
                    platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0)
                    self.platform_group.add(platform)
                if tile == 9:
                    platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1)
                    self.platform_group.add(platform)
                if tile == 10:
                    spikes = Spikes(col_count * tile_size, row_count * tile_size - 150)
                    self.spikes_group.add(spikes)
                if tile == 11:
                    to_tile_list(column1_img_8, tile, col_count, row_count)
                if tile == 12:
                    to_tile_list(column2_img_9, tile, col_count, row_count)
                if tile == 13:
                    door = Door(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                    self.door_group.add(door)
                if tile == 14:
                    enemy = Enemy(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                    self.enemy_group.add(enemy)
                if tile == 15:
                    to_tile_list(stairs_tile_3_right_15, tile, col_count, row_count)
                if tile == 16:
                    to_tile_list(stairs_tile_4_right_16, tile, col_count, row_count)

                if tile == 21:
                    to_tile_list(window_glass_tall_1_21, tile, col_count, row_count)
                if tile == 22:
                    to_tile_list(window_glass_tall_1_22, tile, col_count, row_count)
                if tile == 23:
                    to_tile_list(window_glass_tall_1_23, tile, col_count, row_count)


                col_count += 1
            row_count += 1


    def draw(self):
        self.spikes_group.draw(win)
        self.obstacle_group.draw(win)
        self.platform_group.draw(win)
        self.potion_group.draw(win)
        self.enemy_group.draw(win)
        self.door_group.draw(win)

        for tile in self.tile_list:
            win.blit(tile[0], tile[1])
            #pygame.draw.rect(win, (255, 255, 255), tile[1], 2)



    def move(self, direction):
        self.spikes_group.update(direction)
        self.obstacle_group.update(direction)
        self.platform_group.update(direction)
        self.potion_group.update(direction)
        self.door_group.update(direction)
        self.enemy_group.update(direction)

        for z in range(len(self.tile_list)):
            tile = self.tile_list[z]
            img = tile[0]
            img_rect = tile[1]
            img_rect.x -= direction
            #pygame.draw.rect(win, (255, 255, 255), img_rect, 2)




    def drawgrid(self):
        for line in range(0, 400):
            pygame.draw.line(win, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
            pygame.draw.line(win, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))
