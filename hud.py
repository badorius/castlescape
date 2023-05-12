import pygame
from settings import *

class Hud():

    def __init__(self, live, timer):
        self.width = window_width
        self.height = window_height
        self.width = 500
        self.height = 50
        self.x = 20
        self.y = 20
        self.live = live
        self.timer = timer
        self.font = pygame.font.Font('assets/Fonts/gng.ttf', 40)

        self.bar = pygame.image.load(f"assets/HUD/bar.png")
        self.bar = pygame.transform.scale(self.bar, (self.width, self.height))
        self.bar_background = pygame.image.load(f"assets/HUD/bar_background.png")
        self.bar_background = pygame.transform.scale(self.bar_background, (self.bar.get_width()-10, self.height))
        self.bar_health = pygame.image.load(f"assets/HUD/health_bar.png")
        #self.bar_health = pygame.transform.scale(self.bar_health, (self.live, self.height))
        self.weapon = pygame.image.load(f"assets/HUD/weapon_icon.png")
        #self.weapon = pygame.transform.scale(self.weapon, (1, 1))



    def draw_hud(self, live, score, timer):

        self.font = pygame.font.Font('assets/Fonts/gng.ttf', 40)
        self.title = self.font.render('Tempo Run', True, (220,20,60))
        self.time_left = self.font.render(str(timer), True, (220,20,60))
        self.total_score = self.font.render(str(score), True, (255,255,0))

        #win.blit("Timer", (window_width/2 - self.title.get_width()/2, window_height/2 - title.get_height()/3))
        win.blit(self.weapon, (window_width - self.x - self.weapon.get_height(), self.y))
        win.blit(self.bar_background, (self.x, self.y))
        bar_health = win.blit(self.bar_health, (self.x, self.y))
        if live > 0:
            bar_health = pygame.transform.scale(self.bar_health, (live, self.bar.get_height()))
            win.blit(bar_health, (self.x, self.y))
        else:
            exit()

        win.blit(self.bar, (self.x, self.y))
        win.blit(self.time_left, (window_width - self.x - self.weapon.get_height() * 3, self.y))
        win.blit(self.total_score, (window_width - self.x - self.weapon.get_height() * 8, self.y))

        #screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
