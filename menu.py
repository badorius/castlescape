import pygame
from settings import *
from sounds import *

class Menu():
    def __init__(self, win):
        self.clock = pygame.time.Clock()
        self.game_over_img = pygame.image.load("assets/Background/game_over.png")
        self.status = 0 # 0 main, 1 restart, 3 quit, 4 next

    def draw_level_menu(self, score, timer):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(next_level)

        font = pygame.font.Font('assets/Fonts/gng.ttf', 40)
        #REST FOR TO LOOP SCORE POINTS
        score += timer // 10
        timer -= timer
        title = font.render('Level Completed!!!', True, (255, 0, 0))
        time_left = font.render(str(timer), True, (220, 20, 60))
        total_score = font.render(str(score), True, (255, 255, 0))
        win.blit(title, (window_width / 2 - title.get_width() / 2, window_height / 2 - title.get_height() / 3))
        win.blit(total_score, (window_width / 2 - title.get_width() / 7, window_height / 3 - title.get_height() /5))

        pygame.display.update()

            # hud.draw_hud(ingrid.live, ingrid.score, ingrid.timer)
        title = font.render('Level Completed!!!', True, (255, 0, 0))
        restart_button = font.render('R - Restart', True, (255, 0, 0))
        quit_button = font.render('N - Next', True, (255, 0, 0))
        win.blit(title, (window_width/2 - title.get_width()/2, window_height/2 - title.get_height()/3))
        win.blit(restart_button, (window_width/2 - restart_button.get_width()/2, window_height/1.9 + restart_button.get_height()))
        win.blit(quit_button, (window_width/2 - quit_button.get_width()/2, window_height/2 + quit_button.get_height()/2))
        pygame.display.update()

    def draw_game_over_win(self):
        win.blit(self.game_over_img, (window_width / 6, window_height / 6))
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(game_over)

        #win.fill((0, 0, 0))
        font = pygame.font.Font('assets/Fonts/gng.ttf', 40)
        title = font.render('Game Over', True, (255, 0, 0))
        restart_button = font.render('R - Restart', True, (255, 0, 0))
        quit_button = font.render('Q - Quit', True, (255, 0, 0))
        win.blit(title, (window_width/2 - title.get_width()/2, window_height/2 - title.get_height()/3))
        win.blit(restart_button, (window_width/2 - restart_button.get_width()/2, window_height/1.9 + restart_button.get_height()))
        win.blit(quit_button, (window_width/2 - quit_button.get_width()/2, window_height/2 + quit_button.get_height()/2))
        pygame.display.update()


    def keypress(self):
        run = True
        while run:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                print(run)
                if key[pygame.K_r]:
                    self.status = 1 # restart
                    run = False
                    return self.status
                if key[pygame.K_q]:
                    self.status = 3 # quit
                    run = False
                    return self.status
                if key[pygame.K_n]:
                    self.status = 4 # Next
                    run = False
                    return self.status