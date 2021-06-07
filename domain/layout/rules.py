import pygame as pg
import sys
from pygame.locals import *
from domain.layout import board

class Rules:

    def __init__(self):
        self.bd = board.Board()


    def player(self):
        ''' maak 2 spelers '''
        pass

    def move(self):
        ''' wie is aan zet?'''
        pass

    def win(self):
        ''' wie wint er en hoe kun je winnen'''
        pass

    def valid_space(self):
        ''' zorg ervoor dat elke zet naar het onderste lege vakje wordt geduwd'''
        pass

    def printMouseCoordinates(self, position):
        self.bd.create_canvas().fill(self.bd.white)

        mouseFont = pg.font.SysFont("Helvetica", 32)
        mouseLabel = mouseFont.render(str(position), 1,(self.bd.black))

        self.bd.create_canvas().blit(mouseLabel, (30, 30))
        pg.display.update()


