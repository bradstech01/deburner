import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def colorMaker():
    if random.randint(0,1) == 1:
        colorR = 255
    else:
        colorR = 0
    if random.randint(0,1) == 1:
        colorG = 255
    else:
        colorG = 0
    if random.randint(0,1) == 1:
        colorB = 255
    else:
        colorB = 0
    return (colorR,colorG,colorB)

pygame.init()

DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

mainLoop = True

sizeX, sizeY = DISPLAYSURF.get_size()

while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        if event.type == pygame.KEYDOWN:
            mainLoop = False

    dir = False
    if random.randint(0,1) > 0: dir = True
#    pixel_array = pygame.PixelArray(DISPLAYSURF)
    color = colorMaker()

    if dir:
        x = random.randint(0,sizeX-1)
        for y in range(sizeY):
            DISPLAYSURF.set_at((x,y), color)
    else:
        y = random.randint(0,sizeY-1)
        for x in range(sizeX):
            DISPLAYSURF.set_at((x,y),color)
#    for x in range(0, sizeX-1):
#        for y in range(0, sizeY-1):
#            pixel_array[x][y] = colorMaker()
#    pixel_array.close()
    pygame.display.update()

pygame.quit()
