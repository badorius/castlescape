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

vel = 5
level = 1

# Instance Objects
world = World(world_data_1)
background = Background()
ingrid = Warrior()
skeleton = Enemy()
hud = Hud()

# Vars
floor_y = background.floor1[0].get_height()
ingrid.y -= floor_y
clock = pygame.time.Clock()


def check_collided():
    collide = False

    if (ingrid.x + ingrid.width/2 >= skeleton.x and ingrid.x - ingrid.width/2 <= skeleton.x):
        if (ingrid.y + ingrid.height/2 >= skeleton.y):
            collide = True

    return collide


def redrawGameWindow():
    background.drwaBG()
    hud.draw_hud()
    world.draw()
    #world.drawgrid()

    if hud.live <= 1:
        background.draw_game_over()

    if ingrid.walkCount + 1 >= 24:
        ingrid.walkCount = 0

    if ingrid.idle_floor == 5:
        ingrid.idle = 0
        ingrid.idle_floor = 0

    if skeleton.idle_floor == 5:
        skeleton.idle = 5
        skeleton.idle_floor = 5

    if ingrid.hurt_floor == 3:
        ingrid.hurt = 0
        ingrid.hurt_floor = 0

    if ingrid.left and background.scroll > 0:
        skeleton.move()
        ingrid.update()
        ingrid.walkCount += 1
        background.scroll -= 5
        world.scroll -= 1
        world.move(-5)

    elif ingrid.right and background.scroll < 3000:
        skeleton.move()
        ingrid.update()
        ingrid.walkCount += 1
        background.scroll += 5
        world.scroll += 1
        world.move(5)

    elif background.scroll > 0 or background.scroll < 3000:
        ingrid.idle += 0.2
        ingrid.hurt += 0.2
        skeleton.idle += 0.08
        ingrid.idle_floor = math.floor(ingrid.idle)
        ingrid.hurt_floor = math.floor(ingrid.hurt)
        skeleton.idle_floor = math.floor(skeleton.idle)
        skeleton.move()
        ingrid.update()


        if check_collided():
            win.blit(ingrid.char_hurt[ingrid.hurt_floor], (ingrid.x, ingrid.y))
            if ingrid.face == "Right":
                ingrid.x -= 5
            else:
                ingrid.x += 5

        ingrid.walkCount = 0

    pygame.display.update()


run = True
while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and not world.collide == "left_side":
        if ingrid.x > window_width/8:
            ingrid.x -= vel
        ingrid.left = True
        ingrid.right = False
        ingrid.status = "walk_left"
        if ingrid.face != "Left":
            ingrid.reverse_warrior()
            ingrid.face = "Left"
        skeleton.x += vel - 2


    elif keys[pygame.K_RIGHT] and not world.collide == "right_side":
        if ingrid.x < window_width/2+500 - vel - ingrid.width:
            ingrid.x += vel
        ingrid.left = False
        ingrid.right = True
        ingrid.status = "walk_right"
        if ingrid.face != "Right":
            ingrid.reverse_warrior()
            ingrid.face = "Right"
        skeleton.x -= vel + 2


    else: 
        ingrid.left = False
        ingrid.right = False
        ingrid.walkCount = 0
        skeleton.x -= vel*0.2
        ingrid.status = "idle"

    if keys[pygame.K_LCTRL]:
        ingrid.attack = True
        ingrid.status = "attack"

    if not ingrid.isJump:
        if keys[pygame.K_SPACE]:

            ingrid.isJump = True
            ingrid.status = "jump"
            ingrid.walkCount = 0
            pygame.mixer.Sound.play(ouch)

    else:
        if ingrid.jumpCount >= -10:
            ingrid.y -= (ingrid.jumpCount * abs(ingrid.jumpCount)) * 0.5
            ingrid.jumpCount -= 1
        else:
            ingrid.jumpCount = 10
            ingrid.isJump = False


    world.check_collided_world(ingrid)

    if check_collided():
        if ingrid.status == "attack":
            skeleton.x = window_width - skeleton.width
        else:
            hud.live -= 1
            pygame.mixer.Sound.play(hurt)


    redrawGameWindow()
    
pygame.quit()


