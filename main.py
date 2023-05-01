import pygame
import threading
import level_map
from obstacle import *
from platform import *
import sounds
from gameObject import GameObject
from random import randint
import math
from warrior import Warrior
from obstacle import Obstacle
from platform import Platform
from objects import *
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
platform_group = pygame.sprite.Group()
potion_group = pygame.sprite.Group()
spikes_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
world = World(world_data_1, obstacle_group, platform_group, potion_group, spikes_group, enemy_group)
background = Background()
ingrid = Warrior(screen_width/2, screen_height - 500)
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
        platform_group.draw(win)
        potion_group.draw(win)
        spikes_group.draw(win)
        enemy_group.draw(win)
        #world.drawgrid()

        if ingrid.left and background.scroll > 0:
            background.scroll -= 5
            world.scroll -= 5
            world.move(-5)
            obstacle_group.update(-5)
            platform_group.update(-5)
            potion_group.update(-5)
            spikes_group.update(-5)
            enemy_group.update(-5)


        elif ingrid.right and background.scroll < 6000:
            background.scroll += 5
            world.scroll += 5
            world.move(5)
            obstacle_group.update(+5)
            platform_group.update(+5)
            potion_group.update(+5)
            spikes_group.update(+5)
            enemy_group.update(+5)


        elif background.scroll > 0 or background.scroll < 3000:
            obstacle_group.update(0)
            platform_group.update(0)
            potion_group.update(0)
            spikes_group.update(0)
            enemy_group.update(0)


        ingrid.update(world, obstacle_group, platform_group, potion_group, spikes_group, enemy_group)

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


