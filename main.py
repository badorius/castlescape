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

def main():
    pygame.init()

    # Vars

    clock = pygame.time.Clock()
    level = 1

    # Instance Objects

    world = World(world_data_1)
    background = Background()
    ingrid = Warrior(screen_width/2, screen_height - 500, world)
    hud = Hud(ingrid.live, ingrid.timer)
    menu = Menu(win)


    def redrawGameWindow():

        if ingrid.level_completed:
            menu.draw_level_menu(ingrid.score, ingrid.timer)



        elif ingrid.live <= 1:
            menu.draw_game_over_win()

        elif ingrid.timer <= 0:
            menu.draw_game_over_win()

        else:
            background.drwaBG()
            hud.draw_hud(ingrid.live, ingrid.score, ingrid.timer)
            world.draw()
            ingrid.keypress()
            #world.drawgrid()

            if ingrid.left and background.scroll > 0:
                background.scroll -= vel
                world.move(-vel)

            elif ingrid.right and background.scroll < 6000:
                background.scroll += vel
                world.move(vel)

            elif background.scroll > 0 or background.scroll < 3000:
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
