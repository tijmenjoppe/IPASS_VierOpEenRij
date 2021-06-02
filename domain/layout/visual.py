import pygame as pg
import sys
from pygame.locals import *

black = (0, 0, 0)
white = (255, 255, 255)

pg.init()
gameDisplay = pg.display.set_mode((1000, 800))
gameDisplay.fill(white)
gameDisplay.convert()


def printMouseCoordinates(position):
    pg.draw.circle(position, 50)
    gameDisplay.fill(white)
    mouseFont = pg.font.SysFont("Helvetica", 32)
    mouseLabel = mouseFont.render(str(position), 1, (0, 255,255))
    gameDisplay.blit(mouseLabel, (30, 30))
    pg.display.update()


while True:
    gameDisplay.convert()

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONUP:
            printMouseCoordinates(pg.mouse.get_pos())
    pg.display.update()