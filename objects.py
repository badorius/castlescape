import pygame
from settings import *
from random import randint

class Potion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('assets/Decorations/potion_1.png')
		self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def update(self, x):
		self.rect.x -= x


class Spikes(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('assets/Tiles/spikes.png')
		self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 0
		self.move_counter = 0

	def update(self, x):
		self.rect.y += self.move_direction
		self.rect.x -= x
		self.move_counter += 10
		if abs(self.move_counter) > 300:
			self.move_direction *= -1
			self.move_counter *= -1

class Door(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('assets/Decorations/door.png')
		self.image = pygame.transform.scale(img, (tile_size*2, tile_size*2))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y - tile_size*2 + 25

	def update(self, x):
		self.rect.x -= x
