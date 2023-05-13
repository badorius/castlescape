import pygame

pygame.mixer.init()
pygame.mixer.music.load('assets/music/that-halloween-story.mp3')
pygame.mixer.music.play()
hurt = pygame.mixer.Sound('assets/music/ow.mp3')
jump = pygame.mixer.Sound('assets/music/toy-button-105724.mp3')
attack_sound = pygame.mixer.Sound('assets/music/swinging-staff-whoosh-strong-08-44658.mp3')
game_over = pygame.mixer.Sound('assets/music/videogame-death.mp3')
next_level = pygame.mixer.Sound('assets/music/the-next-level-retro-chiptune-dance-instrumental-space-invaders-137339.mp3')
get_potion = pygame.mixer.Sound('assets/music/potion.mp3')
score_up = pygame.mixer.Sound('assets/music/Point3.mp3')
level_completed_trumped = pygame.mixer.Sound('assets/music/success-trumpets.mp3')


