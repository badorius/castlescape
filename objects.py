import pygame
from settings import *
from random import randint


class Potion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('assets/Decorations/potion_1.png').convert_alpha()
		self.image = pygame.transform.scale_by(img, (3))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def update(self, x):
		self.rect.x -= x


class Spikes(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.size = tile_size * 1
		self.image = pygame.image.load('assets/Tiles/spikes.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (self.size, self.size))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y + self.size * 3
		self.move_direction = 1
		self.move_counter = 0

	def update(self, x):
		self.rect.y += self.move_direction
		self.rect.x -= x
		self.move_counter += 30
		if abs(self.move_counter) > 1000:
			self.move_direction *= -1
			self.move_counter *= -1

class Door(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('assets/Decorations/door.png').convert_alpha()
		self.image = pygame.transform.scale(img, (tile_size*2, tile_size*2))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y - tile_size*2 + 25

	def update(self, x):
		self.rect.x -= x


class Obstacle(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.size = tile_size * 1
		self.image = pygame.image.load('assets/Decorations/sword_2.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (self.size, self.size))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 5
		self.move_counter = 0

	def update(self, x):
		self.rect.y += self.move_direction
		self.rect.x -= x
		self.move_counter += 10
		if abs(self.move_counter) > 300:
			self.move_direction *= -1
			self.move_counter *= -1

class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y, move_x, move_y):
		pygame.sprite.Sprite.__init__(self)
		for i in range(4):
			img1 = pygame.image.load('assets/Tiles/platform_1.png').convert_alpha()
			img2 = pygame.image.load('assets/Tiles/platform_2.png').convert_alpha()
			img3 = pygame.image.load('assets/Tiles/platform_3.png').convert_alpha()
			img4 = pygame.image.load('assets/Tiles/platform_4.png').convert_alpha()

		self.image = pygame.transform.scale(img2, (tile_size, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_counter = 0
		self.move_direction = 1
		self.move_x = move_x
		self.move_y = move_y
		self.collided = False


	def update(self, x):
		self.rect.x += (self.move_direction * self.move_x) - x
		self.rect.y += self.move_direction * self.move_y
		self.move_counter += 1
		if abs(self.move_counter) > 50:
			self.move_direction *= -1
			self.move_counter *= -1


class Key(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.keyimage = []
		self.counter = 0
		for num in range(0, 6):
			self.keyimage.append(pygame.image.load(f'assets/Decorations/Key/tile00{num}.png').convert_alpha())



		self.image = pygame.transform.scale(self.keyimage[self.counter], (tile_size*2, tile_size*2))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y - tile_size*2 + 25

	def update(self, x):
		if self.counter >= 5.0:
			self.counter = 0.0
		else:
			self.counter += 0.1

		img = int(self.counter)
		self.image = pygame.transform.scale(self.keyimage[img], (tile_size*2, tile_size*2))
		self.rect.x -= x


class Torch(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.keyimage = []
		self.counter = 0
		for num in range(0, 6):
			self.keyimage.append(pygame.image.load(f'assets/Decorations/Animated Decorations/torch_big/torch_big_{num}.png').convert_alpha())
		self.image_bg = (pygame.image.load(f'assets/Decorations/Animated Decorations/torch_big/torch_big_background.png').convert_alpha())

		self.image = pygame.transform.scale(self.keyimage[self.counter], (tile_size, tile_size))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y - tile_size*2 + 25

	def update(self, x):
		if self.counter >= 5.0:
			self.counter = 0.0
		else:
			self.counter += 0.1

		img = int(self.counter)
		self.image = pygame.transform.scale(self.keyimage[img], (tile_size, tile_size*2))
		self.rect.x -= x


