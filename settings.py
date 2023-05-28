import pygame
from level_map_1 import *


window_width = 1280
window_height = 800
tile_size = window_width/30
FPS = 60
vel = 5
screen_width = window_width
screen_height = len(world_data_1) * tile_size
pygame.joystick.init()


joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No se encontró ningún gamepad.")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("Gamepad detectado:", joystick.get_name())
    num_axes = joystick.get_numaxes()
    num_buttons = joystick.get_numbuttons()
    num_hats = joystick.get_numhats()
    #print(num_axes, num_buttons, num_hats)


win = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Castle Mania")
#win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)