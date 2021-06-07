import pygame as pg
import sys
from pygame.locals import *
import numpy as np

class Board:

    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        pg.init()

    def create_canvas(self):
        ''' Maak hiermee een doek aan om de game op te maken.'''
        gameDisplay = pg.display.set_mode((1000, 800))
        gameDisplay.fill(self.white)
        gameDisplay.convert()
        pg.display.set_caption("Connect Four")
        return gameDisplay

    def first_screen(self):
        initiating_window = pg.image.load("vieropeenrijcoveredit.png")
        initiating_window = pg.transform.scale(initiating_window, (1000, 800))
        self.create_canvas().blit(initiating_window, (0, 0))
        pg.display.update()


    def board(self):
        board = np.zeros((6,7))
        return board

    def draw_board(self, board):

        for i in range(board.)




