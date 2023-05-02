import pygame
from settings import *
from sounds import *

class Menu():
    def __init__(self, win):
        self.game_over_img = pygame.image.load("assets/Background/game_over.png")


    def draw_start_menu(self):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(next_level)

        font = pygame.font.SysFont('arial', 40)
        title = font.render('Level Completed!!!', True, (255, 255, 255))
        restart_button = font.render('R - Restart', True, (255, 255, 255))
        quit_button = font.render('N - Next', True, (255, 255, 255))
        win.blit(title, (window_width/2 - title.get_width()/2, window_height/2 - title.get_height()/3))
        win.blit(restart_button, (window_width/2 - restart_button.get_width()/2, window_height/1.9 + restart_button.get_height()))
        win.blit(quit_button, (window_width/2 - quit_button.get_width()/2, window_height/2 + quit_button.get_height()/2))
        pygame.display.update()

    def draw_game_over_win(self):
        win.blit(self.game_over_img, (window_width / 6, window_height / 6))
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(game_over)

        #win.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('Game Over', True, (255, 255, 255))
        restart_button = font.render('R - Restart', True, (255, 255, 255))
        quit_button = font.render('Q - Quit', True, (255, 255, 255))
        win.blit(title, (window_width/2 - title.get_width()/2, window_height/2 - title.get_height()/3))
        win.blit(restart_button, (window_width/2 - restart_button.get_width()/2, window_height/1.9 + restart_button.get_height()))
        win.blit(quit_button, (window_width/2 - quit_button.get_width()/2, window_height/2 + quit_button.get_height()/2))
        pygame.display.update()
        self.keypress()


    def keypress(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            print ("Return")
        if key[pygame.K_q]:
            print("quit")
        if key[pygame.K_n]:
            print ("Next")