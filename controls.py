import pygame
from sounds import *
from settings import *



# Cross Button    - Button 0
# Circle Button   - Button 1
# Square Button   - Button 2
# Triangle Button - Button 3
# Left Bumper     - Button 4
# Right Bumper    - Button 5
# L. Trigger(Full)- Button 6
# R. Trigger(Full)- Button 7
# Share Button    - Button 8
# Options Button  - Button 9
# L. Stick In     - Button 10
# R. Stick In     - Button 11
# PS Button       - Button 12
# Touch Pad Click - Button 13


def keypress(ingrid, background, world):
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
        print("attack")

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


def joypress(ingrid, background, world):
    if joystick_count != 0:
        # Cross Button    - Button 0
        # Circle Button   - Button 1
        # Square Button   - Button 2
        # Triangle Button - Button 3
        # Left Bumper     - Button 4
        # Right Bumper    - Button 5
        # L. Trigger(Full)- Button 6
        # R. Trigger(Full)- Button 7
        # Share Button    - Button 8
        # Options Button  - Button 9
        # L. Stick In     - Button 10
        # R. Stick In     - Button 11
        # PS Button       - Button 12
        # Touch Pad Click - Button 13

        if joystick.get_button(0) and ingrid.jumped == False and ingrid.in_air == False:
            pygame.mixer.Sound.play(jump)
            ingrid.vel_y = - 15
            ingrid.jumped = True
            ingrid.left = False
            ingrid.right = False
            ingrid.idle = False
            ingrid.counter += 1
        if joystick.get_button(0) == False:
            ingrid.jumped = False

        if joystick.get_button(1) and ingrid.attack == False:
            pygame.mixer.Sound.play(attack_sound)
            ingrid.attack = True
            ingrid.left = False
            ingrid.right = False
            ingrid.idle = False

        if ingrid.attack == True:
            for z in (0, len(ingrid.images_attack_right)):
                ingrid.counter += 1

        if joystick.get_button(1) == False:
            ingrid.attack = False

        if joystick.get_axis(0) <= -1:
            if background.scroll > 0 and not ingrid.collide_left:
                background.scroll -= vel
                world.move(-vel)
                ingrid.dx -= vel
            ingrid.left = True
            ingrid.right = False
            ingrid.idle = False
            ingrid.counter += 1
            ingrid.direction = -1

        if joystick.get_axis(0) >= 0.5:
            if background.scroll < 6000 and not ingrid.collide_right:
                background.scroll += vel
                world.move(vel)
            ingrid.dx += vel
            ingrid.left = False
            ingrid.right = True
            ingrid.idle = False
            ingrid.counter += 1
            ingrid.direction = 1

        if joystick.get_button(0) == False and joystick.get_button(1) == False and joystick.get_axis(0) == 0:
            ingrid.idle = True
            ingrid.left = False
            ingrid.right = False
            ingrid.attack = False
            ingrid.counter += 1
            # ingrid.index_run = 1

        ingrid.collide_right = False
        ingrid.collide_left = False
