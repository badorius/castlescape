import pygame
from settings import *
from sounds import *
from random import randint

class Bringer(pygame.sprite.Sprite): # Object 14
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size = tile_size * 1
        self.images_right = []
        self.images_left = []
        self.images_death_right = []
        self.images_death_left = []
        self.counter = 0
        self.die = False


        #Sprite RUN
        for num in range(1, 9):
            self.img_right = pygame.image.load(f'assets/Characters/enemy/Bringer-Of-Death/Individual Sprite/Walk/Bringer-of-Death_Walk_{num}.png').convert_alpha()
            self.img_right = pygame.transform.scale_by(self.img_right, (5))
            self.img_left = pygame.transform.flip(self.img_right, True, False)
            self.images_right.append(self.img_right)
            self.images_left.append(self.img_left)

        #Sprite DEATH
        for num in range(1, 11):
            self.image_death_right = pygame.image.load(f'assets/Characters/enemy/Bringer-Of-Death/Individual Sprite/Death/Bringer-of-Death_Death_{num}.png').convert_alpha()
            self.image_death_right = pygame.transform.scale_by(self.image_death_right, (5))
            self.image_death_left = pygame.transform.flip(self.image_death_right, True, False)
            self.images_death_right.append(self.image_death_right)
            self.images_death_left.append(self.image_death_left)


        self.image = self.images_right [self.counter]
        self.image = pygame.transform.scale(self.image, (self.size * 4, self.size * 4))
        self.rect = self.image.get_rect()
        self.rect.width = self.image.get_width()/3
        self.rect.height = self.image.get_height() - tile_size * 1.5
        self.rect.x = x
        self.rect.y = y - tile_size * 2.5
        self.move_direction = 5
        self.move_counter = 0
        self.direction = 1
        self.live = 10

    def killme(self):
        pygame.mixer.Sound.play(enemy1_die)
        self.counter = 0
        self.move_direction = 0
        self.move_counter = 0
        self.die =True



    def update(self, x):

        if not self.die:
            self.move_counter += 5
            if self.counter >= len(self.images_right) - 1:
                self.counter = 0.0
            else:
                self.counter += 0.1
            img = round(self.counter)


            if abs(self.move_counter) > 300:
                self.move_direction *= -1
                if self.move_direction < 0:
                    self.direction = -1
                else:
                    self.direction = 1
                self.move_counter *= -1
            self.rect.x += self.move_direction
            self.rect.x -= x

            if self.counter >= len(self.images_right) - 1:
                self.counter = 0.0
            else:
                self.counter += 0.1
            img = round(self.counter)


            if self.direction == 1:
                self.image = self.images_left[img]
            elif self.direction == -1:
                self.image = self.images_right[img]

            self.image = pygame.transform.scale(self.image, (self.size * 4, self.size * 4))
            win.blit(self.image, (self.rect.x - 10, self.rect.y - 60, self.rect.width, self.rect.height))


        else:
            if self.counter >= len(self.images_death_right) - 1:
                self.kill()
                #self.counter = 0
            else:
                self.counter += 0.1
                img = round(self.counter)

                if self.direction == 1:
                    self.image = self.images_death_left[img]
                else:
                    self.image = self.images_death_right[img]

                self.image = pygame.transform.scale(self.image, (self.size * 4, self.size * 4))
                win.blit(self.image, (self.rect.x - 10, self.rect.y - 60, self.rect.width, self.rect.height))

                self.counter += 0.1


            #pygame.draw.rect(win, (255, 255, 255), self.rect, 2)

            #pygame.draw.rect(win, (255, 255, 255), self.rect, 2)

            #self.counter += 1
            #print(self.move_counter)


class Ghost(pygame.sprite.Sprite): # Object 34
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size = tile_size * 1
        self.images_right = []
        self.images_left = []
        self.images_death_right = []
        self.images_death_left = []
        self.counter = 0
        self.die = False
        self.counter = 0


        #Sprite RUN
        for num in range(1, 5):
            self.img_right = pygame.image.load(f'assets/Characters/enemy/ghost/ghost-{num}.png').convert_alpha()
            self.img_right = pygame.transform.scale_by(self.img_right, (5))
            self.img_left = pygame.transform.flip(self.img_right, True, False)
            self.images_right.append(self.img_right)
            self.images_left.append(self.img_left)

        #Sprite DEATH
        for num in range(1, 6):
            self.image_death_right = pygame.image.load(f'assets/Characters/enemy/enemy-death/enemy-death-{num}.png').convert_alpha()
            self.image_death_right = pygame.transform.scale_by(self.image_death_right, (5))
            self.image_death_left = pygame.transform.flip(self.image_death_right, True, False)
            self.images_death_right.append(self.image_death_right)
            self.images_death_left.append(self.image_death_left)


        self.image = self.images_right [self.counter]
        self.image = pygame.transform.scale(self.image, (self.size * 4, self.size * 4))
        self.rect = self.image.get_rect()
        self.rect.width = self.image.get_width()/3
        self.rect.height = self.image.get_height() - tile_size * 1.5
        self.rect.x = x
        self.rect.y = y - tile_size * 2.5
        self.move_direction = 10
        self.move_counter = 0
        self.direction = 1
        self.live = 10

    def killme(self):
        pygame.mixer.Sound.play(enemy1_die)
        self.counter = 0
        self.move_direction = 0
        self.move_counter = 0
        self.die =True



    def update(self, x):
        if not self.die:

            if self.counter >= len(self.images_right) - 1:
                self.counter = 0.0
            else:
                self.counter += 0.1
            img = round(self.counter)

            self.move_counter += 2

            img = round(self.counter)
            if abs(self.move_counter) > 100:
                self.move_direction *= -1
                if self.move_direction < 0:
                    self.direction = -1
                else:
                    self.direction = 1

                self.move_counter *= -1

            self.rect.x += self.move_direction
            self.rect.x -= x
            if self.counter >= len(self.images_right) - 1:
                self.counter = 0.0
            else:
                self.counter += 0.1
            img = round(self.counter)

            if self.direction == 1:
                self.image = self.images_right[img]
            elif self.direction == -1:
                self.image = self.images_left[img]

            self.image = pygame.transform.scale(self.image, (self.size * 4, self.size * 4))
            win.blit(self.image, (self.rect.x - 10, self.rect.y - 60, self.rect.width, self.rect.height))
            if self.counter >= len(self.images_right) - 1:
                self.counter = 0.0
            else:
                self.counter += 0.1
        else:
            if self.counter > len(self.images_death_right) - 1:
                self.kill()
                #self.counter = 0
            else:
                self.counter += 0.1
                img = round(self.counter)
                if self.direction == 1:
                    self.image = self.images_death_left[img]
                else:
                    self.image = self.images_death_right[img]

                self.image = pygame.transform.scale(self.image, (self.size * 4, self.size * 4))
                win.blit(self.image, (self.rect.x - 10, self.rect.y - 60, self.rect.width, self.rect.height))

                #self.counter += 1


            #pygame.draw.rect(win, (255, 255, 255), self.rect, 2)

            #pygame.draw.rect(win, (255, 255, 255), self.rect, 2)

            #self.counter += 1
            #print(self.move_counter)


class Gato(pygame.sprite.Sprite): # Object 35
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size = tile_size * 1
        self.images_right = []
        self.images_left = []
        self.images_death_right = []
        self.images_death_left = []
        self.counter = 0
        self.die = False


        #Sprite RUN
        for num in range(1, 14):
            self.img_right = pygame.image.load(f'assets/Characters/enemy/hell-gato/hellgato-{num}.png').convert_alpha()
            self.img_right = pygame.transform.scale_by(self.img_right, (2))
            self.img_left = pygame.transform.flip(self.img_right, True, False)
            self.images_right.append(self.img_right)
            self.images_left.append(self.img_left)

        #Sprite DEATH
        for num in range(1, 6):
            self.image_death_right = pygame.image.load(f'assets/Characters/enemy/enemy-death/enemy-death-{num}.png').convert_alpha()
            self.image_death_right = pygame.transform.scale_by(self.image_death_right, (5))
            self.image_death_left = pygame.transform.flip(self.image_death_right, True, False)
            self.images_death_right.append(self.image_death_right)
            self.images_death_left.append(self.image_death_left)


        self.image = self.images_right [self.counter]
        #self.image = pygame.transform.scale_by(self.image, 2)
        self.rect = self.image.get_rect()
        self.rect.width = self.image.get_width() / 1.2
        self.rect.height = self.image.get_height() - tile_size
        self.rect.x = x - tile_size / 2
        self.rect.y = y - tile_size * 1.4
        self.move_direction = 10
        self.move_counter = 0
        self.direction = 1
        self.live = 10

    def killme(self):
        pygame.mixer.Sound.play(enemy1_die)
        self.counter = 0
        self.move_direction = 0
        self.move_counter = 0
        self.die =True



    def update(self, x):
        if not self.die:

            if self.counter >= len(self.images_right) - 1:
                self.counter = 0.0
            else:
                self.counter += 0.1
            img = round(self.counter)

            self.move_counter += 5

            if abs(self.move_counter) > 300:
                self.move_direction *= -1
                if self.move_direction < 0:
                    self.direction = -1
                else:
                    self.direction = 1
                self.move_counter *= -1

            self.rect.x += self.move_direction
            self.rect.x -= x

            if self.counter >= len(self.images_right) - 1:
                self.counter = 0

            if self.direction == 1:
                self.image = self.images_left[img]
            elif self.direction == -1:
                self.image = self.images_right[img]

                #self.image = pygame.transform.scale(self.image, (self.size * 2, self.size * 2))
            self.counter += 0.1
            win.blit(self.image, (self.rect.x - 20, self.rect.y - 40, self.rect.width, self.rect.height))
            #pygame.draw.rect(win, (255, 255, 255), self.rect, 2)


        else:
            if self.counter > len(self.images_death_right) - 1:
                self.kill()
                #self.counter = 0
            else:
                self.counter += 0.1
                img = round(self.counter)
                if self.direction == 1:
                    self.image = self.images_death_left[img]
                else:
                    self.image = self.images_death_right[img]

                self.image = pygame.transform.scale(self.image, (self.size * 4, self.size * 4))
                win.blit(self.image, (self.rect.x - 10, self.rect.y - 60, self.rect.width, self.rect.height))


            #pygame.draw.rect(win, (255, 255, 255), self.rect, 2)

        #pygame.draw.rect(win, (255, 255, 255), self.rect, 2)

            #self.counter += 1
            #print(self.move_counter)
