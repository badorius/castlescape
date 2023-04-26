import pygame

import level_map
from gameObject import GameObject
from random import randint
import math
from warrior import Warrior
from enemy import Enemy
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
ghost_group = pygame.sprite.Group()
world = World(world_data_1, ghost_group)
background = Background()
ingrid = Warrior(100, screen_height - 130)
hud = Hud()


def redrawGameWindow():
    background.drwaBG()
    hud.draw_hud()
    world.draw()
    ghost_group.update()
    ghost_group.draw(win)
    #world.drawgrid()

    if hud.live <= 1:
        background.draw_game_over()

    if ingrid.left and background.scroll > 0:
        ingrid.update(world)
        background.scroll -= 5
        world.scroll -= 1
        world.move(-5)

    elif ingrid.right and background.scroll < 3000:
        ingrid.update(world)
        background.scroll += 5
        world.scroll += 1
        world.move(5)

    elif background.scroll > 0 or background.scroll < 3000:
        ingrid.update(world)

    pygame.display.update()


run = True
while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redrawGameWindow()
    
pygame.quit()


