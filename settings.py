import pygame
from level_map_1 import *


window_width = 1280
window_height = 800
tile_size = window_width/30
FPS = 60
vel = 5
screen_width = window_width
screen_height = len(world_data_1) * tile_size


win = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Castle Mania")