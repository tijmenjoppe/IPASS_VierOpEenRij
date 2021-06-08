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


    def win(self, player):

        board = self.board
        for i in range(7-3):
            for j in range(6):
                if board[j][i] == board[j][i+1] and board[j][i+1] == board[j][i+2] and board[j][i+2] == board[j][i+3] and board[j][i] == player:
                    return self.player

        for i in range(7):
            for j in range(6-3):
                if board[j][i] == board[j+1][i] and board[j+1][i] == board[j+2][i] and board[j+2][i] == board[j+3][i] and board[j][i] == player:
                    return self.player

        for i in range(7-3):
            for j in range(6-3):
                if board[j][i] == board[j+1][i+1] and board[j+1][i+1] == board[j+2][i+2] and board[j+2][i+2] == board[j+3][i+3] and board[j][i] == player:
                    return self.player

        for i in range(7-3):
            for j in range(3, 6):
                if board[j][i] == board[j-1][i+1] and board[j-1][i+1] == board[j-2][i+2] and board[j-2][i+2] == board[j-3][i+3] and board[j][i] == player:
                        return self.player

    def player_click(self, posx, board, player):
        if posx < 100:
            self.move(player, 0, self.last_open_position(board, 0))
        elif posx < 200 and posx > 100:
            self.move(player, 1, self.last_open_position(board, 1))
        elif posx < 300 and posx > 200:
            self.move(player,2, self.last_open_position(board, 2))
        elif posx < 400 and posx > 300:
            self.move(player, 3, self.last_open_position(board, 3))
        elif posx < 500 and posx > 400:
            self.move(player, 4, self.last_open_position(board, 4))
        elif posx < 600 and posx > 500:
            print('used')
            self.move(player, 5, self.last_open_position(board, 5))

    def last_open_position(self, board, x):
        for index, row in enumerate( board ):
            if row[x] == 1 or row[x] == 2:
                continue
            else:
                return index

    def move(self, player, x, y):
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
                        # red
                        self.bd.print_board(self.board)
                        self.player_click(posx, self.board, self.player )
                        self.bd.draw_board(self.board, self.player)
                        if self.win(self.player) == 1:
                            print("red wins")
                            sys.exit()
                    else:
                        # yellow
                        self.player = 2
                        self.player_click(posx, self.board, self.player)
                        self.bd.draw_board(self.board, self.player )
                        if self.win(self.player) == 2:
                            print("yellow wins")
                            sys.exit()

                    self.player += 1
                    self.player = self.player % 2




