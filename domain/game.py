from layout import board

import pygame as pg
import sys
import numpy as np
from pygame.locals import *
import time

class Game:

    def __init__(self):
        self.bd = board.Board()
        self.board = np.zeros((6, 7))
        self.player = 0

    def player(self):
        ''' maak 2 spelers '''
        pass

    def win(self):
        ''' wie wint er en hoe kun je winnen'''
        pass

    def player_click(self, posx, posy, board, player):
        if posx < 100:
            self.move(player, 0, self.last_open_position(board, 1))
        elif posx < 200 and posx > 100:
            self.move(player, 1, self.last_open_position(board, 2))
        elif posx < 300 and posx > 200:
            self.move(player,2, self.last_open_position(board, 3))
        elif posx < 400 and posx > 300:
            self.move(player, 3, self.last_open_position(board, 4))
        elif posx < 500 and posx > 400:
            self.move(player, 4, self.last_open_position(board, 5))
        elif posx < 600 and posx > 500:
            self.move(player, 5, self.last_open_position(board, 6))

    def last_open_position(self, board, x):
        for i in board[x]:
            if i == 1 or i == 2:
                continue
            else:
                return i

    def move(self, player, x, y):
        print(player, x, y)
        self.board[int(y)][x] = player

    def connect_four_game(self):

        pg.init()
        self.bd.first_screen()
        self.bd.draw_board(self.board, self.player)
        pg.display.update()

        while True:

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    posx, posy = pg.mouse.get_pos()
                    if self.player == 1:
                        self.bd.print_board(self.board)
                        self.player_click(posx, posy, self.board, self.player )

                        #red
                        self.bd.draw_board(self.board, self.player)
                    else:
                        self.player = 2
                        self.player_click(posx, posy, self.board, self.player)
                        #yellow
                        self.bd.draw_board(self.board, self.player )

                    self.player += 1
                    self.player = self.player % 2




