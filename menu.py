import pygame
from settings import *
from sounds import *
from time import *

class Menu():
    def __init__(self):
        self.game_over_img = pygame.image.load("assets/Background/game_over.png")
        self.game_main_img = pygame.image.load("assets/Background/Menu/night-town-background-previewx2.png")
        self.game_main_img = pygame.transform.scale(self.game_main_img, (window_width, window_height))
        self.status = 0 # 0 main, 1 restart, 3 quit, 4 next, 5 run

    def draw_level_menu(self):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(level_completed_trumped)
        font = pygame.font.Font('assets/Fonts/gng.ttf', 40)
        title = font.render('Level Completed!!!', True, (255, 0, 0))
        win.blit(title, (window_width / 2 - title.get_width() / 2, window_height / 2 - title.get_height() / 3))
        pygame.display.update()


    def draw_game_over_win(self):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(game_over)
        #win.blit(self.game_over_img, (window_width / 6, window_height / 6))
        #win.fill((0, 0, 0))
        font = pygame.font.Font('assets/Fonts/gng.ttf', 40)
        title = font.render('Game Over', True, (255, 0, 0))
        restart_button = font.render('R - Restart', True, (255, 0, 0))
        main_button = font.render('M - Main Menu', True, (255, 0, 0))
        quit_button = font.render('Q - Quit', True, (255, 0, 0))
        win.blit(title, (window_width/2 - title.get_width()/2, window_height/3 - title.get_height()/3))
        win.blit(restart_button, (window_width/2 - restart_button.get_width()/2, window_height/2.5 + restart_button.get_height()))
        win.blit(main_button, (window_width/2 - main_button.get_width()/2, window_height/2 + main_button.get_height()))
        win.blit(quit_button, (window_width/2 - quit_button.get_width()/2, window_height/1.5 + quit_button.get_height()/2))
        pygame.display.update()


    def main_menu(self):
        #pygame.mixer.music.load('assets/music/that-halloween-story.mp3')
        #pygame.mixer.music.play()
        win.blit(self.game_main_img, (window_width /100, window_height/100))
        font = pygame.font.Font('assets/Fonts/gng.ttf', 40)
        title = font.render('', True, (255, 0, 0))
        restart_button = font.render('S - Start Game', True, (255, 0, 0))
        quit_button = font.render('Q - Quit', True, (255, 0, 0))
        win.blit(title, (window_width/2 - title.get_width()/2, window_height/2 - title.get_height()/3))
        win.blit(restart_button, (window_width/2 - restart_button.get_width()/2, window_height/1.9 + restart_button.get_height()))
        win.blit(quit_button, (window_width/2 - quit_button.get_width()/2, window_height/2 + quit_button.get_height()/2))
        pygame.display.update()


    def keypress(self):
        #event = pygame.event.wait()
        #if event.type == pygame.QUIT:
        #    pygame.quit()

        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.status == 3:
                    run = False
                if self.status != 1 or self.status != 2 or self.status != 3 or self.status != 4 or self.status != 5:
                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.get_pressed()
                        if key[pygame.K_r]:
                            self.status = 1  # restart
                            return self.status
                        if key[pygame.K_q]:
                            self.status = 3  # quit
                            return self.status
                        if key[pygame.K_n]:
                            self.status = 4  # Next
                            return self.status
                        if key[pygame.K_s]:
                            self.status = 5  # run
                            return self.status
                else:
                    run = False
