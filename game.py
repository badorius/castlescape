import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy
from background import Background

class Game:


    def __init__(self):
        self.width = 1440
        self.height = 900
        self.white_colour = (255, 255, 255)
        self.FPS = 60

        self.game_window = pygame.display.set_mode((self.width,self.height))

        self.clock = pygame.time.Clock()


        self.level = 1.0

        self.reset_map()

        pygame.mixer.init()
        pygame.mixer.music.load('assets/music/04.mp3')
        pygame.mixer.music.play()
        self.ouch = pygame.mixer.Sound('assets/music/jump.mp3')
        self.isJump = False


    def reset_map(self):
        self.player = Player((self.width / 2), (self.height - 100), 100, 100, 10)
        self.background = Background(0, 0, self.width, self.height, 1)
        speed = 5 + (self.level * 5)

        if self.level >= 4.0:
            self.enemies = [
                Enemy(0, 600, 50, 50, speed),
                Enemy(750, 400, 50, 50, speed),
                Enemy(0, 200, 50, 50, speed),
            ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(0, 600, 50, 50, speed),
                Enemy(750, 400, 50, 50, speed),
            ]
        else:
            self.enemies = [
                Enemy(0, 600, 50, 50, speed),
            ]


    def draw_objects(self, player_direction):
        self.game_window.fill(self.white_colour)
        self.game_window.scroll(10,10)


        self.game_window.blit(self.background.image1, (self.background.x1, self.background.y1))
        self.game_window.blit(self.background.image2, (self.background.x2, self.background.y2))
        self.game_window.blit(self.background.image3, (self.background.x3, self.background.y3))

        self.game_window.blit(self.player.image, (self.player.x, self.player.y))

        #self.game_window.blit(self.player.walkRight[player_direction//3], (self.player.x, self.player.y))

        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))

        pygame.display.update()


    def move_objects(self, player_direction, isJump):

        self.player.move(player_direction, self.width)
        self.background.move((player_direction * -1), self.width)
        for enemy in self.enemies:
            enemy.move(self.width)


    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
        if self.detect_collision(self.player, enemy):
            self.level += 0.5
            return True
        return False


    def detect_collision(self, object_1, object_2):

        if object_1.y < (object_2.y + object_2.height) and (object_1.y + object_1.height) > object_2.y and object_1.x < (object_2.x + object_2.width) and (object_1.x + object_1.width) > object_2.x:
            return True
        return False


    def run_game_loop(self):
        player_direction = 0

        while True:

            # Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player_direction = -1
                    elif event.key == pygame.K_RIGHT:
                        player_direction = 1
                    elif event.key == pygame.K_SPACE:
                        player_direction = 0
                        self.isJump = True
                        pygame.mixer.Sound.play(self.ouch)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                        player_direction = 0

                    

            # Execute logic
            self.move_objects(player_direction, self.isJump)

            # Update display
            self.draw_objects(player_direction)

            # Detect collisions
            if self.check_if_collided():
                self.reset_map()

            self.clock.tick(self.FPS)