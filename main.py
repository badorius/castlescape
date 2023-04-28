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
ingrid = Warrior(screen_width/2 - 55, screen_height)
hud = Hud()


def redrawGameWindow():
    background.drwaBG()
    hud.draw_hud()
    world.draw()
    ghost_group.update()
    ghost_group.draw(win)
    world.drawgrid()


    if hud.live <= 1:
        background.draw_game_over()

    if ingrid.left and background.scroll > 0:
        ingrid.update(world)
        background.scroll -= 5
        world.scroll -= 5
        world.move(-5)

    elif ingrid.right and background.scroll < 6000:
        ingrid.update(world)
        background.scroll += 5
        world.scroll += 5
        world.move(5)

    elif background.scroll > 0 or background.scroll < 3000:
        ingrid.update(world)

    pygame.display.update()

def keypress():
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and ingrid.jumped == False:
        pygame.mixer.Sound.play(ouch)
        ingrid.vel_y = -15
        ingrid.jumped = True
        ingrid.idle = False

    if key[pygame.K_SPACE] == False:
        ingrid.jumped = False

    if key[pygame.K_LEFT]:
        ingrid.left = True
        ingrid.right = False
        ingrid.idle = False
        ingrid.dx -= 5
        ingrid.counter += 1
        ingrid.direction = -1
    if key[pygame.K_RIGHT]:
        ingrid.left = False
        ingrid.right = True
        ingrid.idle = False
        ingrid.dx += 5
        ingrid.counter += 1
        ingrid.direction = 1

    if key[pygame.K_LCTRL]:
        ingrid.attack = True
        pygame.mixer.Sound.play(ouch)

    if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and key[pygame.K_LCTRL] == False:
        ingrid.idle = True
        ingrid.attack = False
        ingrid.left = False
        ingrid.right = False
        ingrid.counter = 0
        ingrid.index_run = 0


run = True
while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keypress()
    redrawGameWindow()
    
pygame.quit()


