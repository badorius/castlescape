import pygame
from gameObject import GameObject
from random import randint

pygame.init()
window_width = 1280
window_height = 800
x = 400
y = 700
width = 100
height = 100
vel = 5
FPS = 60
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
scroll = 0

pygame.mixer.init()
pygame.mixer.music.load('assets/music/04.mp3')
pygame.mixer.music.play()
ouch = pygame.mixer.Sound('assets/music/jump.mp3')

win = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("First Game")

walkLeft = []
walkRight = []
char = []
bgs = []
floor1 = []



for z in range(1,10):
    walkRight.append(pygame.image.load(f"assets/Characters/knight/walk/walk_knight_{z}.png"))
    walkRight[z-1] = pygame.transform.scale(walkRight[z-1], (width, height))

for z in range(1,10):
    walkLeft.append(pygame.image.load(f"assets/Characters/knight/walk/walk_knight_{z}.png"))
    walkLeft[z-1] = pygame.transform.scale(walkLeft[z-1], (width, height))
    walkLeft[z-1] = pygame.transform.flip(walkLeft[z-1], 1, 0)

for z in range(1,7):
    char.append(pygame.image.load(f"assets/Characters/knight/walk/walk_knight_{z}.png"))
    char[z-1] = pygame.transform.scale(char[z-1], (width, height))

for z in range(1,4):
    bgs.append(pygame.image.load(f"assets/Background/layer_{z}.png"))
    if z is not 3:
        bgs[z-1] = pygame.transform.scale(bgs[z-1], (window_width, window_height))
    elif z is 3:
        bgs[z - 1] = pygame.transform.scale(bgs[z - 1], (window_width, bgs[z-1].get_height()))

for z in range(1,5):
    floor1.append(pygame.image.load(f"assets/Tiles/floor_tile_{z}.png"))

floor_y = floor1[0].get_height()
y -= floor_y


clock = pygame.time.Clock()

def drwaBG():
    for x in range(5):
        speed = 1
        for bg in bgs:
            if bgs.index(bg) is not 2:
                win.blit(bg, ((x*window_width) - scroll * speed, 0))
                speed += 0.2
            elif bgs.index(bg) is 2:
                win.blit(bg, ((x*window_width) - scroll * speed, window_height - 60))
                speed += 0.2


def  draw_ground():
    floor_rnd = randint(1, 10)
    for z in range(1000):

        for x in range(1,5):
            win.blit(floor1[x-1], (x+z * (floor1[x-1].get_width()) - scroll * 2.2, window_height - floor1[x-1].get_height()))

def redrawGameWindow():
    global walkCount
    global scroll

    drwaBG()
    draw_ground()

    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left and scroll > 0:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
        scroll -= 5

    elif right and scroll < 3000:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
        scroll += 5

    elif scroll > 0 or scroll < 3000:
        win.blit(char[walkCount//3],  (x, y))
        walkCount = 0
        
    pygame.display.update()

run = True

while run:

    clock.tick(FPS)

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

    if not isJump:
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

    redrawGameWindow() 
    
    
pygame.quit()


