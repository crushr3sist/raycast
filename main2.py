import pygame, random, math, os, math
import numpy as np
from time import sleep
from colors import colors
from mapSetup import DrawMap
from Rays import Ray

WIDTH = 1280
HEIGHT = 960
FPS = 120

pygame.init()
pygame.mixer.init()
os.environ["SDL_VIDEO_WINDOW_POS"] = "%i,%i" % (0.5, 100)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()

map = DrawMap(screen)
ray = Ray(WIDTH, HEIGHT, screen)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            ray.player_x += ray.pdx
            ray.player_y += ray.pdy

        if keys_pressed[pygame.K_a]:
            ray.player_angle += 5
            ray.player_angle = ray.fixAngle(ray.player_angle)
            ray.pdx = math.cos(ray.degToRad(ray.player_angle)) * 5
            ray.pdy = -math.sin(ray.degToRad(ray.player_angle)) * 5

        if keys_pressed[pygame.K_s]:
            ray.player_x -= ray.pdx
            ray.player_y -= ray.pdy

        if keys_pressed[pygame.K_d]:
            ray.player_angle -= 5
            ray.player_angle = ray.fixAngle(ray.player_angle)
            ray.pdx = math.cos(ray.degToRad(ray.player_angle)) * 5
            ray.pdy = -math.sin(ray.degToRad(ray.player_angle)) * 5

    screen.fill(colors.GREY())
    player = pygame.Rect(ray.player_x - 25, ray.player_y - 25, 50, 50)
    ray.drawRays(map.returnWalls())
    map.draw()
    pygame.draw.ellipse(screen, colors.YELLOW(), player, 25)

    pygame.display.flip()

pygame.quit()
