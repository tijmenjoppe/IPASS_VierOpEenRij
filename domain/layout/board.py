import pygame as pg
import sys
from pygame.locals import *
import time
import numpy as np

class Board:

    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.height = 700
        self.width = 700
        self.gameDisplay = pg.display.set_mode((self.height, self.width))
        self.set_difficulty = None
        self.start_the_game = None

    def print_board(self, board):
        print(np.flip(board, 0))

    def first_screen(self):
        initiating_window = pg.image.load("vieropeenrijcoveredit.png")
        initiating_window = pg.transform.scale(initiating_window, (self.height, self.width))
        pg.display.set_caption("Connect Four")
        self.gameDisplay.blit(initiating_window, (0, 0))
        pg.display.update()
        time.sleep(1)
        self.gameDisplay.fill(self.black)

    def first_menu(self):
        self.gameDisplay.fill(self.white)
        lettertype = pg.font.SysFont( "monospace", 30 )
        label_qstn = lettertype.render("Kies een gamemode", 1, self.black)
        label_AI = lettertype.render( "VS AI", 1, self.black )
        label_PLAYER = lettertype.render("VS PLAYER", 1, self.black)
        self.gameDisplay.blit(label_AI, (150, 300))
        self.gameDisplay.blit(label_PLAYER, (400, 300))
        self.gameDisplay.blit(label_qstn, (200, 100))
        pg.display.update()

    def ai_menu(self):
        self.gameDisplay.fill( self.white )
        lettertype = pg.font.SysFont( "monospace", 30 )
        label_qstn = lettertype.render( "Kies een kleur", 1, self.black )
        label_AI = lettertype.render( "rood", 1, self.red )
        label_PLAYER = lettertype.render( "geel", 1, self.yellow )
        self.gameDisplay.blit( label_AI, (150, 300) )
        self.gameDisplay.blit( label_PLAYER, (400, 300) )
        self.gameDisplay.blit( label_qstn, (200, 100) )
        pg.display.update()
    def draw_board(self, board, player):

        for i in range(7):
            for j in range(6):
                x = i * 100 + 100 / 2
                y = j * 100 + 100 + 100 / 2
                pg.draw.rect(self.gameDisplay, self.blue, (i * 100, j * 100 + 100, 100, 100))
                pg.draw.circle(self.gameDisplay, self.black, (x, y), 100/2-5)

        for i in range(7):
            x = i * 100 + 100 / 2
            y = 100 / 2
            if player == 2:
                pg.draw.circle( self.gameDisplay, self.red, (x, y), 100 / 2 - 5)
            if player == 1:
                pg.draw.circle( self.gameDisplay, self.yellow, (x, y), 100 / 2 - 5)

        for i in range(7):
            for j in range(6):
                x = i * 100 + 100 / 2
                y = j * 100 + 100 + 100 / 2
                if board[j][i] == 1:
                    pg.draw.circle(self.gameDisplay, self.red, (x,y), 100 / 2 - 5)
                if board[j][i] == 2:
                    pg.draw.circle( self.gameDisplay, self.yellow, (x,y), 100 / 2 - 5)

        pg.display.update()

    def error_message(self):
        lettertype = pg.font.SysFont( "monospace", 60 )
        label = lettertype.render( "Not possible", 1, self.white )
        self.gameDisplay.blit(label, (40, 10))





