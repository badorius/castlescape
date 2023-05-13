import pygame
import threading
from random import randint
import math
from warrior import Warrior
from world1 import *
from world2 import *
from background1 import *
from background2 import *
from settings import *
from sounds import *
from menu import *
from hud import *
from level_map_1 import *
from level_map_2 import *

def main():
    pygame.init()

    # Vars and Instance Objects
    world_level = 1
    clock = pygame.time.Clock()
    world = World1(world_level)
    ingrid = Warrior(screen_width/2, screen_height - 500, world)
    background = Background1(world_level)
    hud = Hud(ingrid.live, ingrid.timer)
    menu = Menu(win)

    def keypress():
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and ingrid.jumped == False and ingrid.in_air == False:
            pygame.mixer.Sound.play(jump)
            ingrid.vel_y = - 15
            ingrid.jumped = True
            ingrid.left = False
            ingrid.right = False
            ingrid.idle = False
            ingrid.counter += 1
        if key[pygame.K_SPACE] == False:
            ingrid.jumped = False

        if key[pygame.K_LCTRL]:
            pygame.mixer.Sound.play(attack_sound)
            ingrid.attack = True
            ingrid.left = False
            ingrid.right = False
            ingrid.idle = False
            for z in (0, len(ingrid.images_attack_right)):
                ingrid.counter += 1

        if key[pygame.K_LEFT]:
            if background.scroll > 0 and not ingrid.collide_left:
                background.scroll -= vel
                world.move(-vel)
                ingrid.dx -= vel
            ingrid.left = True
            ingrid.right = False
            ingrid.idle = False
            ingrid.counter += 1
            ingrid.direction = -1

        if key[pygame.K_RIGHT]:
            if background.scroll < 6000 and not ingrid.collide_right:
                background.scroll += vel
                world.move(vel)
            ingrid.dx += vel
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
            # ingrid.index_run = 1

        ingrid.collide_right = False
        ingrid.collide_left = False

    def redrawGameWindow():

        if ingrid.level_completed:
            menu.draw_level_menu(ingrid.score, ingrid.timer)
            ingrid.level += 1
            global world_level
            world_level = ingrid.level
            print (world_level)

        elif ingrid.live <= 1:
            menu.draw_game_over_win()

        elif ingrid.timer <= 0:
            menu.draw_game_over_win()

        else:
            background.drwaBG()
            hud.draw_hud(ingrid.live, ingrid.score, ingrid.timer)
            world.draw()
            keypress()
            ingrid.check_collide()
            ingrid.update()
            #world.drawgrid()
            #if background.scroll > 0 or background.scroll < 3000:
            world.move(0)


        pygame.display.update()


    run = True
    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if menu.status == 1:
                main()
            if event.type == pygame.QUIT or menu.status == 3:
                run = False
        redrawGameWindow()

    pygame.quit()


if __name__ == "__main__":
    main()
