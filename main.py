import pygame, random, math, os, math
import numpy as np
from time import sleep

# https://www.youtube.com/watch?v=gYRrGTC7GtA

WIDTH = 1280
HEIGHT = 960
FPS = 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (155, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 255)
GREY = (25,25,25)
YELLOW = (255,255,0)

MAP = [
    [1,1,1,1,1,1,1,1,1,1,],
    [1,0,0,0,0,0,0,0,0,1,],
    [1,0,2,0,0,0,0,0,0,1,],
    [1,0,2,0,0,0,0,0,0,1,],
    [1,0,2,0,0,0,0,0,0,1,],
    [1,0,2,0,0,0,0,0,0,1,],
    [1,0,0,0,0,0,0,0,0,1,],
    [1,0,0,0,0,0,0,0,0,1,],
    [1,0,0,0,0,0,0,0,0,1,],
    [1,1,1,1,1,1,1,1,1,1,],
]

def drawMap():
    bricks = []
    lines = []
    brick_width = 128
    brick_height = 96
    color = None
    for y in range(0,len(MAP)):
        for x in range(len(MAP[y])):
            if MAP[y][x] == 1:
                color = GREEN
                x_pos = x * brick_width
                y_pos = y * brick_height
                bricks.append((pygame.Rect(x_pos, y_pos, brick_width, brick_height), color))
                lines.append((pygame.Rect(x_pos, y_pos, 5, brick_height), BLACK))
                lines.append((pygame.Rect(x_pos, y_pos, brick_width, 5), BLACK))
            if MAP[y][x] == 2:
                color = RED
                x_pos = x * brick_width
                y_pos = y * brick_height
                bricks.append((pygame.Rect(x_pos, y_pos, brick_width, brick_height), color))
                lines.append((pygame.Rect(x_pos, y_pos, 5, brick_height), BLACK))
                lines.append((pygame.Rect(x_pos, y_pos, brick_width, 5), BLACK))
                lines.append((pygame.Rect(x_pos+brick_width, y_pos, 5, brick_height+5), BLACK))
                lines.append((pygame.Rect(x_pos, y_pos+brick_height, brick_width, 5), BLACK))
    for objs in bricks:
        pygame.draw.rect(screen, objs[1], objs[0])
    for line in lines:
        pygame.draw.rect(screen, line[1], line[0])

def degToRad(angle):
    return angle * math.pi / 180

def fixAngle(angle):
    if angle > 359:
        angle -= 360
    if angle < 0 :
        angle += 360
    return angle

def drawRays(player_x, player_y, pdx, pdy):
    rays = []
    position_vector = pygame.math.Vector2(player_x, player_y)
    lines_height = 40
    x = player_x + pdx * 20
    y = player_y + pdy * 20
    print(x, y)

    pygame.draw.line(screen, WHITE, position_vector, (x,y), 5)

def calcInter():
    pass


pygame.init()
pygame.mixer.init()  ## For sound
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (0.5, 100)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()   


## Game loop
pdx = 0
pdy = 0
player_angle = 0
player_x = WIDTH/ 2
player_y = HEIGHT/ 2

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            running = False

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w]:
            player_x  += pdx
            player_y  += pdy
            print(pdx, pdy)

        if keys_pressed[pygame.K_a]:
            player_angle += 5
            player_angle = fixAngle(player_angle)
            pdx = math.cos(degToRad(player_angle))* 5
            pdy = -math.sin(degToRad(player_angle)) * 5
            print(pdx, pdy)

        if keys_pressed[pygame.K_s]:
            player_x  -= pdx
            player_y  -= pdy
            print(pdx, pdy)
            
        if keys_pressed[pygame.K_d]:
            player_angle -= 5
            player_angle = fixAngle(player_angle)
            pdx = math.cos(degToRad(player_angle))* 5
            pdy = -math.sin(degToRad(player_angle)) * 5
            print(pdx, pdy)

    screen.fill(GREY)
    player = pygame.Rect(player_x-25,player_y-25, 50,  50)
    drawMap()
    drawRays(player_x, player_y, pdx, pdy)
    calcInter()
    pygame.draw.ellipse(screen, YELLOW, player, 25)
    pygame.display.flip() 

pygame.quit()