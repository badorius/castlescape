import pygame
import threading
from random import randint
import math

import world1
from warrior import Warrior
from enemy import *
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
    
    clock = pygame.time.Clock()

    # Vars and Instance Objects
    level = 1
    world = World1(level)
    ingrid = Warrior(screen_width/2, screen_height - 500, world)
    background = Background1(level)
    hud = Hud(ingrid.live, ingrid.timer)
    menu = Menu()

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

        if key[pygame.K_LCTRL] and ingrid.attack == False:
            pygame.mixer.Sound.play(attack_sound)
            ingrid.attack = True
            ingrid.left = False
            ingrid.right = False
            ingrid.idle = False

        if ingrid.attack == True:
            for z in (0, len(ingrid.images_attack_right)):
                ingrid.counter += 1
        if key[pygame.K_LCTRL] == False:
            ingrid.attack = False

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
            #LOOP SCORE
            ingrid.score += 10
            # score += timer // 10
            ingrid.timer -= 10
            if ingrid.timer < 0:
                ingrid.timer = 0

            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(score_up)
            background.drwaBG()
            hud.draw_hud(ingrid.live, ingrid.score, ingrid.timer)
            world.draw()
            # world.drawgrid()
            # if background.scroll > 0 or background.scroll < 3000:
            world.move(0)

            if ingrid.timer <= 0:
                global level
                ingrid.level_completed = False
                menu.status = 4
                run_menu()

                ingrid.level += 1
                level = ingrid.level
                world.reset(level)
                background.reset(level)
                ingrid.reset(screen_width / 2, screen_height - 500, world)
                redrawGameWindow()

        elif ingrid.live <= 1:
            menu.draw_game_over_win()
            menu.keypress()
            run_menu()

        elif ingrid.timer <= 0:
            menu.draw_game_over_win()
            menu.keypress()
            run_menu()

        else:
            background.drwaBG()
            hud.draw_hud(ingrid.live, ingrid.score, ingrid.timer)
            world.draw()
            keypress()
            check_collide()
            ingrid.update()
            #world.drawgrid()
            #if background.scroll > 0 or background.scroll < 3000:
            world.move(0)
        pygame.display.update()

    def run_menu():
        # 0 main, 1 restart, 3 quit, 4 next, 5 run, 6 gameover
        if menu.status != 5:
            if menu.status == 0:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(sounds.songs[0])
                pygame.mixer.music.play()
                menu.main_menu()
                menu.keypress()
                ingrid.level = 1
                level = ingrid.level
                world.reset(level)
                background.reset(level)
                ingrid.reset(screen_width / 2, screen_height - 500, world)
            if menu.status == 1:
                menu.status == 5
                ingrid.level = 1
                level = ingrid.level
                world.reset(level)
                background.reset(level)
                ingrid.reset(screen_width / 2, screen_height - 500, world)
                redrawGameWindow()

            if menu.status == 3:
                global run
                run = False

            if menu.status == 4:
                menu.draw_level_menu()
                menu.keypress()
                pygame.mixer.music.play()

        else:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(sounds.songs[ingrid.level])
            pygame.mixer.music.play()


    def check_collide():
        ingrid.in_air = True
        col_thresh = 20
        ingrid.dx = 0
        ingrid.dy = 0
        # check for collision
        for tile in world.tile_list:
            # check for collision in x direction
            if ingrid.direction == 1:
                if tile[1].colliderect(ingrid.rect.x + ingrid.dx + vel, ingrid.rect.y - vel, ingrid.rect.width, ingrid.rect.height):
                    #self.dx = -vel
                    ingrid.collide_right = True
            if ingrid.direction == -1:
                if tile[1].colliderect(ingrid.rect.x + ingrid.dx - vel, ingrid.rect.y - vel, ingrid.rect.width, ingrid.rect.height):
                    #self.dx = vel
                    ingrid.collide_left = True

            #print(self.collide_right, self.collide_left)

            # check for collision in y direction
            if tile[1].colliderect(ingrid.rect.x, ingrid.rect.y + ingrid.dy, ingrid.rect.width, ingrid.rect.height):
                #print("collide y")
                # check if below the ground i.e. jumping
                if ingrid.vel_y < - 15:
                    ingrid.dy = tile[1].bottom - ingrid.rect.top
                    ingrid.vel_y = 0
                # check if above the ground i.e. falling
                elif ingrid.vel_y >= 0:
                    ingrid.dy = tile[1].top - ingrid.rect.bottom
                    ingrid.vel_y = 0
                    ingrid.in_air = False


            # Check collide obstacle
            if pygame.sprite.spritecollide(ingrid, world.obstacle_group, False):
                ingrid.collide_obstacle = True
                pygame.mixer.Sound.play(hurt)
                ingrid.live -= 0.01
                if ingrid.direction == 1:
                    ingrid.dx -= 0.01
                if ingrid.direction == -1:
                    ingrid.dx += 0.01
            else:
                ingrid.collide_obstacle = False

            # Check collide enemy
            if ingrid.attack == True:
                collided_enemies = pygame.sprite.spritecollide(ingrid, world.enemy_group, False)
                for enemy in collided_enemies:
                    pygame.mixer.Sound.play(enemy1_die)
                    enemy.killme()
                    ingrid.collide_enemy = False
                    ingrid.score += 10
            else:
                if pygame.sprite.spritecollide(ingrid, world.enemy_group, False):
                    ingrid.collide_enemy = True
                    pygame.mixer.Sound.play(hurt)
                    ingrid.live -= 0.01
                    if ingrid.direction == 1:
                        ingrid.dx -= 0.01
                    if ingrid.direction == -1:
                        ingrid.dx += 0.01


            # Check spikes collide
            if pygame.sprite.spritecollide(ingrid, world.spikes_group, False):
                ingrid.collide_spikes = True
                pygame.mixer.Sound.play(hurt)
                ingrid.live -= 0.01
                if ingrid.direction == 1:
                    ingrid.dy -= 0.01
                if ingrid.direction == -1:
                    ingrid.dy += 0.01
            else:
                ingrid.collide_spikes = False

            # check for collision with platforms
            for platform in world.platform_group:
                # collision in the x direction
                if platform.rect.colliderect(ingrid.rect.x + ingrid.dx, ingrid.rect.y, ingrid.rect.width, ingrid.rect.height):
                    ingrid.dx = 0
                # collision in the y direction
                if platform.rect.colliderect(ingrid.rect.x, ingrid.rect.y + ingrid.dy, ingrid.rect.width, ingrid.rect.height):
                    # check if below platform
                    if abs((ingrid.rect.top + ingrid.dy) - platform.rect.bottom) < col_thresh:
                        ingrid.vel_y = 0
                        ingrid.dy = platform.rect.bottom - ingrid.rect.top
                    # check if above platform
                    elif abs((ingrid.rect.bottom + ingrid.dy) - platform.rect.top) < col_thresh:
                        ingrid.rect.bottom = platform.rect.top
                        ingrid.in_air = False
                        ingrid.dy = 0
                        ingrid.counter += 1

                    # move sideways with the platform
                    if platform.move_x != 0:
                        ingrid.rect.x += platform.move_direction

            # FALL DOWN
            if ingrid.rect.y > window_height - tile_size * 2:
                pygame.mixer.Sound.play(hurt)
                ingrid.collide_obstacle = True
                ingrid.live -= 0.01
            else:
                ingrid.collide_obstacle = False

            # Collide Potion 
            if pygame.sprite.spritecollide(ingrid, world.potion_group, True):
                if ingrid.live < ingrid.live_max - 50:
                    pygame.mixer.Sound.play(get_potion)
                    ingrid.live += 50
                else:
                    ingrid.live = ingrid.live_max
                    pygame.mixer.Sound.play(get_potion)

            # Collide Door
            if pygame.sprite.spritecollide(ingrid, world.door_group, False):
                ingrid.level_completed = True


    run_menu()
    ingrid.level = 1
    pygame.mixer.music.stop()
    pygame.mixer.music.load(sounds.songs[ingrid.level])
    pygame.mixer.music.play()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or menu.status == 3:
                run = False

        redrawGameWindow()


    pygame.quit()


if __name__ == "__main__":
    main()
