import pygame

pygame.mixer.init()
pygame.mixer.music.load('assets/music/background/2020-02-04_-_Powerful_-_David_Fesliyan.mp3')
pygame.mixer.music.play()
ouch = pygame.mixer.Sound('assets/music/fast-simple-chop-5-6270.mp3')
hurt = pygame.mixer.Sound('assets/music/female_hurt-87490.mp3')
