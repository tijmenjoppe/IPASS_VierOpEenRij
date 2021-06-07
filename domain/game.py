from layout import board
from layout import rules
import pygame as pg
import sys
from pygame.locals import *
import time

class Game:

    def __init__(self):
        self.bd = board.Board()
        self.rl = rules.Rules()

    def connect_four_game(self):
        board = self.bd.board()
        player = None
        pg.init()
        self.bd.first_screen()

        self.bd.draw_board(board, player)
        pg.display.update()

        while True:

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

