import pygame
from gameObject import GameObject

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
    bgs[z-1] = pygame.transform.scale(bgs[z-1], (window_width, window_height))



clock = pygame.time.Clock()

def redrawBG():

    for z in range(0,6):

        for bg in bgs:
            index = bgs.index(bg) + 1
            bg_x = ((window_width * z) - x) * index
            print(bg_x)
            win.blit(bg, (bg_x, 0))


def redrawGameWindow():
    global walkCount

    redrawBG()
    

    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1

    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1

    else:
        win.blit(char[walkCount//3], (x, y))
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


