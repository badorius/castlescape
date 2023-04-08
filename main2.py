import pygame
from gameObject import GameObject

pygame.init()
window_width = 1280
window_height = 800

pygame.mixer.init()
pygame.mixer.music.load('assets/music/04.mp3')
pygame.mixer.music.play()
ouch = pygame.mixer.Sound('assets/music/jump.mp3')


win = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('assets/Characters/knight/walk/walk_knight_1.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_2.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_3.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_4.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_5.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_6.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_7.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_8.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_9.png')]
walkLeft = [pygame.image.load('assets/Characters/knight/walk/walk_knight_1.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_2.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_3.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_4.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_5.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_6.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_7.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_8.png'), pygame.image.load('assets/Characters/knight/walk/walk_knight_9.png')]
bgs = [pygame.image.load('assets/Background/layer_1.png'), pygame.image.load('assets/Background/layer_2.png'), pygame.image.load('assets/Background/layer_3.png'),  ]
char = [pygame.image.load('assets/Characters/knight/idle/idle_knight_1.png'), pygame.image.load('assets/Characters/knight/idle/idle_knight_2.png'), pygame.image.load('assets/Characters/knight/idle/idle_knight_3.png'), pygame.image.load('assets/Characters/knight/idle/idle_knight_4.png'), pygame.image.load('assets/Characters/knight/idle/idle_knight_5.png'), pygame.image.load('assets/Characters/knight/idle/idle_knight_6.png')]

x = 400
y = 700
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount

    for bg in bgs:
        bgimage = pygame.transform.scale(bg, (window_width, window_height))
        win.blit(bgimage, (0,0))

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
    clock.tick(27)

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
        
    if not(isJump):
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


