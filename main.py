import pygame

import level_map
import obstacle
import sounds
from gameObject import GameObject
from random import randint
import math
from warrior import Warrior
from obstacle import Obstacle
from world import World
from background import Background
from settings import *
from sounds import *
from hud import *
from level_map import *

pygame.init()

# Vars

clock = pygame.time.Clock()
vel = 5
level = 1

# Instance Objects
obstacle_group = pygame.sprite.Group()
world = World(world_data_1, obstacle_group)
background = Background()
ingrid = Warrior(screen_width/2 - 55, screen_height)
hud = Hud(ingrid.live)


def redrawGameWindow():

    if ingrid.live <= 1:
        win.blit(hud.game_over_img, (window_width / 6, window_height / 6))
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(game_over)

    else:

        background.drwaBG()
        hud.draw_hud(ingrid.live)
        world.draw()
        obstacle_group.draw(win)
        # world.drawgrid()

        if ingrid.left and background.scroll > 0:
            background.scroll -= 5
            world.scroll -= 5
            world.move(-5)
            ingrid.update(world, obstacle_group)
            obstacle_group.update(-5)

        elif ingrid.right and background.scroll < 6000:
            background.scroll += 5
            world.scroll += 5
            world.move(5)
            ingrid.update(world, obstacle_group)
            obstacle_group.update(+5)



        elif background.scroll > 0 or background.scroll < 3000:
            ingrid.update(world, obstacle_group)
            obstacle_group.update(0)


    pygame.display.update()

def keypress():
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and ingrid.jumped == False:
        if ingrid.jump_counter < 2:
            ingrid.jump_counter += 1
            ingrid.counter += 1
            pygame.mixer.Sound.play(ouch)
            ingrid.vel_y = -15
            ingrid.jumped = True
            ingrid.left = False
            ingrid.right = False
            ingrid.idle = False
        elif ingrid.vel_y == 0:
            ingrid.jump_counter = 0
    if key[pygame.K_SPACE] == False:
        ingrid.jumped = False


    if key[pygame.K_LCTRL]:
        pygame.mixer.Sound.play(ouch)
        ingrid.attack = True
        ingrid.left = False
        ingrid.right = False
        ingrid.idle = False
        ingrid.counter += 1

    if key[pygame.K_LEFT]:
        ingrid.dx -= 5
        ingrid.left = True
        ingrid.right = False
        ingrid.idle = False
        ingrid.counter += 1
        ingrid.direction = -1


    if key[pygame.K_RIGHT]:
        ingrid.dx += 5
        ingrid.left = False
        ingrid.right = True
        ingrid.idle = False
        ingrid.counter += 1
        ingrid.direction = 1


    if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and key[pygame.K_LCTRL] == False:
        ingrid.idle = True
        ingrid.left = False
        ingrid.right = False
        ingrid.attack = False
        ingrid.counter += 1
        #ingrid.index_run = 1


run = True
while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keypress()
    redrawGameWindow()
    
pygame.quit()


