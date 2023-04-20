import pygame
from settings import *

class Hud():

    def __init__(self):
        self.width = window_width
        self.height = window_height
        self.width = 500
        self.height = 50
        self.x = 20
        self.y = 20
        self.live = 500

        self.bar = pygame.image.load(f"assets/HUD/bar.png")
        self.bar = pygame.transform.scale(self.bar, (self.width, self.height))
        self.bar_background = pygame.image.load(f"assets/HUD/bar_background.png")
        self.bar_background = pygame.transform.scale(self.bar_background, (self.bar.get_width()-10, self.height))
        self.bar_health = pygame.image.load(f"assets/HUD/health_bar.png")
        #self.bar_health = pygame.transform.scale(self.bar_health, (self.live, self.height))
        self.weapon = pygame.image.load(f"assets/HUD/weapon_icon.png")
        #self.weapon = pygame.transform.scale(self.weapon, (1, 1))
