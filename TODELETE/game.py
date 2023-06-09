import pygame
from TODELETE.player import Player
from TODELETEobstacle import Enemy
from TODELETEbackground import Background


class Game:


    def __init__(self):
        self.width = 800
        self.height = 432
        self.white_colour = (255, 255, 255)
        self.FPS = 60
        self.scroll = 0
        self.level = 1.0
        self.x = self.width / 2
        self.y = self.height - 100
        self.flor = self.y

        self.game_window = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()



        self.reset_map()

        pygame.mixer.init()
        pygame.mixer.music.load('../assets/music/04.mp3')
        pygame.mixer.music.play()
        self.ouch = pygame.mixer.Sound('../assets/music/jump.mp3')


        self.isJump = False
        self.isLeft = False
        self.isRight = False


    def reset_map(self):
        x = self.width / 2
        y = self.height - 100
        self.player = Player(self.x, self.flor, 100, 100, 10)
        self.background = Background(0, 0, self.width, self.height, 1)
        speed = 5 + (self.level * 5)

        if self.level >= 4.0:
            self.enemies = [
                Enemy(0, self.height - 200, 50, 50, speed),
                Enemy(750, self.height - 200, 50, 50, speed),
                Enemy(0, self.height - 200, 50, 50, speed),
            ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(0, self.height - 200, 50, 50, speed),
                Enemy(750, self.height - 200, 50, 50, speed),
            ]
        else:
            self.enemies = [
                Enemy(0, self.height - 200, 50, 50, speed),
            ]


    def draw_objects(self, player_direction):
        self.game_window.fill(self.white_colour)
        self.game_window.scroll(10,10)

        for x in range (5):
            for i in range(0, self.background.bg_num):
                #self.game_window.blit(self.background.bg_images[i], ((self.background.x_list[i] * self.background.bg_with_list[i]) - player_direction, self.background.y_list[i]))
                self.game_window.blit(self.background.bg_images[i], ((self.width * x) + self.background.x_list[i], self.background.y_list[i]))

        if self.isRight:
            self.game_window.blit(self.player.walkRight[player_direction//3], (self.player.x, self.player.y))
            self.isRight = False
        elif self.isLeft:
            self.game_window.blit(self.player.walkLeft[player_direction//3], (self.player.x, self.player.y))
            #self.isLeft = False

        elif self.isJump:
            for up in self.player.jump_y:
                self.game_window.blit(self.player.char[player_direction//3], (self.player.x, up))
            if self.player.y is not self.flor:
                print(f"{self.player.y} is not {self.flor}")
            self.isJump = False
        else:
            self.game_window.blit(self.player.char[player_direction//3], (self.player.x, self.player.y))


        #self.game_window.blit(self.player.walkRight[player_direction//3], (self.player.x, self.player.y))

        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))

        pygame.display.update()


    def move_objects(self, player_direction):
        if self.isLeft or self.isRight:
            self.player.move(player_direction, self.width/2)
        elif self.isJump:
            self.player.jump(player_direction, self.width/2)



        #self.player.jump(player_direction, self.width/2)
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
            self.clock.tick(self.FPS)

            # Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player_direction = -1
                        self.isLeft = True
                        self.isRight = False
                    elif event.key == pygame.K_RIGHT:
                        player_direction = 1
                        self.isRight = True
                        self.isLeft = False
                    elif event.key == pygame.K_SPACE:
                        player_direction = 0
                        self.isJump = True
                        pygame.mixer.Sound.play(self.ouch)
                        self.player.jump(player_direction, self.width)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                        player_direction = 0

    def run_game_loop_new(self):
        run = True

        while run:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and x > vel:
                x -= vel
                left = True
                right = False

            elif keys[pygame.K_RIGHT] and x < 1280 - vel - width:
                x += vel
                left = False
                right = True

            else:
                left = False
                right = False
                walkCount = 0

            if not (isJump):
                if keys[pygame.K_SPACE]:
                    isJump = True
                    left = False
                    right = False
                    walkCount = 0
                    pygame.mixer.Sound.play(ouch)

            else:
                if jumpCount >= -10:
                    y -= (jumpCount * abs(jumpCount)) * 0.5
                    jumpCount -= 1
                else:
                    jumpCount = 10
                    isJump = False

                    

            # Execute logic
            self.move_objects(player_direction)

            # Update display
            self.draw_objects(player_direction)

            # Detect collisions
            if self.check_if_collided():
                self.reset_map()

