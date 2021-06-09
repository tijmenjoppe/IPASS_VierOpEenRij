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
        self.gamemode = 0
        self.ai = 0


    def win(self, player):
        b = self.board
        for i in range(7-3):
            for j in range(6):
                if b[j][i] == b[j][i+1] and b[j][i+1] == b[j][i+2] and b[j][i+2] == b[j][i+3] and b[j][i] == player:
                    return self.player

        for i in range(7):
            for j in range(6-3):
                if b[j][i] == b[j+1][i] and b[j+1][i] == b[j+2][i] and b[j+2][i] == b[j+3][i] and b[j][i] == player:
                    return self.player

        for i in range(7-3):
            for j in range(6-3):
                if b[j][i] == b[j+1][i+1] and b[j+1][i+1] == b[j+2][i+2] and b[j+2][i+2] == b[j+3][i+3] and b[j][i] == player:
                    return self.player

        for i in range(7-3):
            for j in range(3, 6):
                if b[j][i] == b[j-1][i+1] and b[j-1][i+1] == b[j-2][i+2] and b[j-2][i+2] == b[j-3][i+3] and b[j][i] == player:
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
            self.move(player, 5, self.last_open_position(board, 5))
        elif posx < 700 and posx > 600:
            self.move(player, 6, self.last_open_position(board, 6))

    def last_open_position(self, board, x):
        for index, row in enumerate(board):
            if row[x] == 1 or row[x] == 2:
                continue
            else:
                return index

    def move(self, player, x, y):
        if y == None:
            return -1
        self.board[int(y)][x] = player

    def game_loop(self):
        self.bd.gameDisplay.fill( self.bd.black )
        self.bd.draw_board( self.board, self.player )
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
                        self.player_click( posx, self.board, self.player )
                        self.bd.draw_board( self.board, self.player )
                        if self.win( self.player ) == 1:
                            self.bd.print_board( self.board )
                            print( "red wins" )
                            sys.exit()
                    else:
                        # yellow
                        self.player = 2
                        self.player_click( posx, self.board, self.player )
                        self.bd.draw_board( self.board, self.player )
                        if self.win( self.player ) == 2:
                            self.bd.print_board( self.board )
                            print( "yellow wins" )
                            sys.exit()
                    self.bd.print_board( self.board )
                    self.player += 1
                    self.player = self.player % 2

    def connect_four_game(self):

        pg.init()
        self.bd.first_screen()
        pg.display.update()
        self.bd.first_menu()
        pg.display.update()

        while self.gamemode == 0:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    posx, posy = pg.mouse.get_pos()
                    if posx < 350:
                        self.bd.ai_menu()
                        while self.gamemode == 0:
                            for event in pg.event.get():
                                if event.type == QUIT:
                                    pg.quit()
                                    sys.exit()
                                if event.type == pg.MOUSEBUTTONDOWN:
                                    posx, posy = pg.mouse.get_pos()
                                    if posx < 350:
                                        self.gamemode = 1
                                        self.player = 2
                                        self.ai = 1
                                        self.game_loop()
                                    else:
                                        self.gamemode = 1
                                        self.player = 1
                                        self.ai = 2
                                        self.game_loop()
                    else:
                        self.gamemode = 1
                        self.game_loop()






