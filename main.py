import pygame
from gameObject import GameObject
from random import randint
import math
from warrior import Warrior
from enemy import Enemy
from settings import *
from sounds import *
from hud import *

pygame.init()

vel = 5
scroll = 0
level = 1


win = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("First Game")

bgs = []
floor1 = []



for z in range(1,4):
    bgs.append(pygame.image.load(f"assets/Background/layer_{z}.png"))
    if z != 3:
        bgs[z-1] = pygame.transform.scale(bgs[z-1], (window_width, window_height))
    elif z == 3:
        bgs[z - 1] = pygame.transform.scale(bgs[z - 1], (window_width, bgs[z-1].get_height()))

for z in range(1,5):
    floor1.append(pygame.image.load(f"assets/Tiles/floor_tile_{z}.png"))


ingrid = Warrior()
skeleton = Enemy()
hud = Hud()
floor_y = floor1[0].get_height()
ingrid.y -= floor_y


clock = pygame.time.Clock()

def drwaBG():
    for x in range(10):
        speed = 1
        for bg in bgs:
            if bgs.index(bg) != 2:
                win.blit(bg, ((x*window_width) - scroll * speed, 0))
                speed += 0.2
            elif bgs.index(bg) == 2:
                win.blit(bg, ((x*window_width) - scroll * speed, window_height - 60))
                speed += 0.2


def  draw_ground():
    floor_rnd = randint(1, 10)
    for z in range(1000):

        for x in range(1,5):
            win.blit(floor1[x-1], (x+z * (floor1[x-1].get_width()) - scroll * 2.2, window_height - floor1[x-1].get_height()))


def draw_hud():
    win.blit(hud.weapon, (window_width - hud.x - hud.weapon.get_height() , hud.y))
    win.blit(hud.bar_background, (hud.x, hud.y))
    bar_health = win.blit(hud.bar_health, (hud.x, hud.y))
    if hud.live > 0:
        bar_health = pygame.transform.scale(hud.bar_health, (hud.live, hud.bar.get_height()))
        win.blit(bar_health, (hud.x, hud.y))
    else:
        exit()

    win.blit(hud.bar, (hud.x, hud.y))


def redrawGameWindow():
    global scroll

    drwaBG()
    draw_ground()
    draw_hud()

    if ingrid.walkCount + 1 >= 24:
        ingrid.walkCount = 0

    if ingrid.idle_floor == 5:
        ingrid.idle = 0
        ingrid.idle_floor = 0

    if skeleton.idle_floor == 5:
        skeleton.idle = 5
        skeleton.idle_floor = 5

    if ingrid.hurt_floor == 3:
        ingrid.hurt = 0
        ingrid.hurt_floor = 0


    if ingrid.isJump:
        print(" ingrid is jump")


    if ingrid.left and scroll > 0:
        if ingrid.attack:
            win.blit(ingrid.char_attack[ingrid.attackCount], (ingrid.x, ingrid.y))
        else:
            win.blit(ingrid.walkLeft[ingrid.walkCount//3], (ingrid.x, ingrid.y))

        win.blit(skeleton.char[skeleton.idle_floor], (skeleton.x, skeleton.y))
        ingrid.walkCount += 1
        scroll -= 5


    elif ingrid.right and scroll < 3000:
        if ingrid.attack:
            win.blit(ingrid.char_attack[ingrid.attackCount], (ingrid.x, ingrid.y))
        else:
            win.blit(ingrid.walkRight[ingrid.walkCount//3], (ingrid.x, ingrid.y))

        win.blit(skeleton.char[skeleton.idle_floor], (skeleton.x, skeleton.y))
        ingrid.walkCount += 1
        scroll += 5

    elif scroll > 0 or scroll < 3000:
        ingrid.idle += 0.2
        ingrid.hurt += 0.2
        skeleton.idle += 0.08
        ingrid.idle_floor = math.floor(ingrid.idle)
        ingrid.hurt_floor = math.floor(ingrid.hurt)
        skeleton.idle_floor = math.floor(skeleton.idle)
        win.blit(skeleton.char[skeleton.idle_floor], (skeleton.x, skeleton.y))
        if ingrid.attack:
            win.blit(ingrid.char_attack[ingrid.attackCount], (ingrid.x, ingrid.y))
        else:
            win.blit(ingrid.char[ingrid.idle_floor], (ingrid.x, ingrid.y))

        if check_collided():
            win.blit(ingrid.char_hurt[ingrid.hurt_floor], (ingrid.x, ingrid.y))
        ingrid.walkCount = 0


        
    pygame.display.update()

def check_collided():
    collide = False
    #print(ingrid.y, skeleton.y)

    if (ingrid.x + ingrid.width/2 >= skeleton.x and ingrid.x - ingrid.width/2 <= skeleton.x):
        if (ingrid.y + ingrid.height/2 >= skeleton.y):
            collide = True

    return collide

run = True
while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        if ingrid.x > window_width/4:
            ingrid.x -= vel
        ingrid.left = True
        ingrid.right = False
        if ingrid.face != "Left":
            ingrid.reverse_warrior()
            ingrid.face = "Left"
        skeleton.x += vel

    elif keys[pygame.K_RIGHT]:
        if ingrid.x < window_width/2+200 - vel - ingrid.width:
            ingrid.x += vel
        ingrid.left = False
        ingrid.right = True
        if ingrid.face != "Right":
            ingrid.reverse_warrior()
            ingrid.face = "Right"
        skeleton.x -= vel

    else: 
        ingrid.left = False
        ingrid.right = False
        ingrid.walkCount = 0
        skeleton.x -= vel*0.2

    if not ingrid.attack:
        if keys[pygame.K_LCTRL]:
            ingrid.attack = True
            ingrid.attackCount = 0
            pygame.mixer.Sound.play(ouch)

    else:
        if ingrid.attackCount < 11:
            ingrid.attackCount += 1
        else:
            ingrid.attackCount = 0
            ingrid.attack = False

    if not ingrid.isJump:
        if keys[pygame.K_SPACE]:
            ingrid.isJump = True
            ingrid.walkCount = 0
            pygame.mixer.Sound.play(ouch)

    else:
        if ingrid.jumpCount >= -10:
            ingrid.y -= (ingrid.jumpCount * abs(ingrid.jumpCount)) * 0.5
            ingrid.jumpCount -= 1
        else: 
            ingrid.jumpCount = 10
            ingrid.isJump = False

    if check_collided():
        hud.live -= 1
        pygame.mixer.Sound.play(hurt)



    redrawGameWindow()
    
    
pygame.quit()


