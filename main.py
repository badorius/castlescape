import pygame
import threading
from random import randint
import math
from warrior import Warrior
from world import World
from background import Background
from settings import *
from sounds import *
from menu import *
from hud import *
from level_map import *

pygame.init()

# Vars

clock = pygame.time.Clock()
vel = 5
level = 1

# Instance Objects

world = World(world_data_1)
background = Background()
ingrid = Warrior(screen_width/2, screen_height - 500)
hud = Hud(ingrid.live)
menu = Menu(win)


def redrawGameWindow():

    if ingrid.level_completed:
        menu.draw_start_menu()

    elif ingrid.live <= 1:
        menu.draw_game_over_win()

    elif hud.timer <= 0:
        menu.draw_game_over_win()

    else:
        background.drwaBG()
        hud.draw_hud(ingrid.live)
        world.draw()
        #world.drawgrid()

        if ingrid.left and background.scroll > 0:
            background.scroll -= 5
            world.move(-5)

        elif ingrid.right and background.scroll < 6000:
            background.scroll += 5
            world.move(5)

        elif background.scroll > 0 or background.scroll < 3000:
            world.move(0)

        ingrid.update(world)

    pygame.display.update()


run = True
while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ingrid.keypress()
    redrawGameWindow()
    
pygame.quit()


