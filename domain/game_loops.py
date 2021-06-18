import math
from layout import board
import random
import pygame as pg
import sys
import numpy as np
from pygame.locals import *
import time


class Game_Loops:

    def __init__(self):
        self.bd = board.Board()
        self.board = np.zeros( (6, 7) )
        self.player = 0
        self.gamemode = 0
        self.ai = 0
        self.game_turn = 0
        self.dict_best_moves = {}

    def terminal_node(self, board, player, ai):
        return self.win( player ) or self.win( ai ) or len( self.open_positions( board ) ) == 0

    def minimax(self, board, depth, alpha, beta, maximizingPlayer, ai, player):

        options = self.open_positions( board )

        if depth == 0 or self.terminal_node( board, player, ai ):
            if self.terminal_node(board, player, ai):
                if self.win(player) == player:
                    return -10000000, options
                if self.win(ai) == ai:
                    return 10000000, options
            return self.evaluate_position( board, ai ), options

        if maximizingPlayer:
            maxEval = -math.inf
            bestOption = None
            for option in options:
                board_copy = board.copy()
                self.move( ai, option[0], option[1], board_copy )
                evalresult = self.minimax( board_copy, depth - 1, alpha, beta, False, ai, player )[0]
                # if depth >= 2:
                #     print(board_copy, depth, option, evalresult)
                if evalresult > maxEval:
                    maxEval = evalresult
                    bestOption = option
                maxEval = max( maxEval, evalresult )
                alpha = max( alpha, evalresult )
                if beta <= alpha:
                    break
            return maxEval, bestOption

        else:
            minEval = math.inf
            worstOption = None
            for option in options:
                board_copy = board.copy()
                self.move( player, option[0], option[1], board_copy )
                evalresult = self.minimax( board_copy, depth - 1, alpha, beta, True, ai, player )[0]
                # if depth >= 2:
                    # print( board_copy, depth, option, evalresult  )
                if evalresult < minEval:
                    minEval = evalresult
                    worstOption = option
                minEval = min( minEval, evalresult )
                beta = min( beta, evalresult )
                if beta <= alpha:
                    break
            return minEval, worstOption

    def ai_move(self):
        move = self.minimax( self.board, 5, -math.inf, math.inf, True, self.ai, self.player )[1]
        self.move( self.ai, move[0], move[1], self.board )
        self.dict_best_moves = {}
        print( "AI move" )

    def choice(self, options):
        return random.choice( options )

    def open_positions(self, board):
        lst_options = []

        for x in range( 7 ):
            for y in range( 5, -1, -1 ):
                if board[y][x] == 0.0:
                    tuplexy = x, y
                    lst_options.append( tuplexy )
                    break
        return lst_options

    def evaluate_position(self, board, player):
        score = 0
        b = board

        middle = [int( i ) for i in list( board[:, 7 // 2] )]
        middle_amount = middle.count( player )
        score += 100 * middle_amount

        for i in range( 7 - 3 ):
            for j in range( 6 ):
                lst = [b[j][i], b[j][i + 1], b[j][i + 2], b[j][i + 3]]
                score += self.score_position( lst, player )

        for i in range( 7 ):
            for j in range( 6 - 3 ):
                lst = [b[j][i], b[j + 1][i], b[j + 2][i], b[j + 3][i]]
                score += self.score_position( lst, player )

        for i in range( 7 - 3 ):
            for j in range( 6 - 3 ):
                lst = [b[j][i], b[j + 1][i + 1], b[j + 2][i + 2], b[j + 3][i + 3]]
                score += self.score_position( lst, player )

        for i in range( 7 - 3 ):
            for j in range( 3, 6 ):
                lst = [b[j][i], b[j - 1][i + 1], b[j - 2][i + 2], b[j - 3][i + 3]]
                score += self.score_position( lst, player )

        return score

    def score_position(self, lst, player):
        score = 0
        opponent = self.player

        if lst.count( player ) == 4:
            score += 1000000000000000
        if lst.count( player ) == 3 and lst.count( 0 ) == 1:
            score += 900
        if lst.count( player ) == 2 and lst.count(0) == 2:
            score += 400
        if lst.count( opponent ) == 3 and lst.count( 0 ) == 1:
            score -= 900
        if lst.count( opponent ) == 4:
            score -= 10000000000000000

        return score

    def win(self, player):
        b = self.board
        for i in range( 7 - 3 ):
            for j in range( 6 ):
                if b[j][i] == b[j][i + 1] and b[j][i + 1] == b[j][i + 2] and b[j][i + 2] == b[j][i + 3] and b[j][
                    i] == player:
                    return player

        for i in range( 7 ):
            for j in range( 6 - 3 ):
                if b[j][i] == b[j + 1][i] and b[j + 1][i] == b[j + 2][i] and b[j + 2][i] == b[j + 3][i] and b[j][
                    i] == player:
                    return player

        for i in range( 7 - 3 ):
            for j in range( 6 - 3 ):
                if b[j][i] == b[j + 1][i + 1] and b[j + 1][i + 1] == b[j + 2][i + 2] and b[j + 2][i + 2] == b[j + 3][
                    i + 3] and b[j][i] == player:
                    return player

        for i in range( 7 - 3 ):
            for j in range( 3, 6 ):
                if b[j][i] == b[j - 1][i + 1] and b[j - 1][i + 1] == b[j - 2][i + 2] and b[j - 2][i + 2] == b[j - 3][
                    i + 3] and b[j][i] == player:
                    return player

    def player_click(self, posx, board, player):
        if posx < 100:
            self.move( player, 0, self.last_open_position( board, 0 ), self.board )
        elif posx < 200 and posx > 100:
            self.move( player, 1, self.last_open_position( board, 1 ), self.board )
        elif posx < 300 and posx > 200:
            self.move( player, 2, self.last_open_position( board, 2 ), self.board )
        elif posx < 400 and posx > 300:
            self.move( player, 3, self.last_open_position( board, 3 ), self.board )
        elif posx < 500 and posx > 400:
            self.move( player, 4, self.last_open_position( board, 4 ), self.board )
        elif posx < 600 and posx > 500:
            self.move( player, 5, self.last_open_position( board, 5 ), self.board )
        elif posx < 700 and posx > 600:
            self.move( player, 6, self.last_open_position( board, 6 ), self.board )

    def last_open_position(self, board, x):
        for y in range( 5, -1, -1 ):
            if board[y][x] == 0.0:
                return y

    def move(self, player, x, y, board):
        if y == None:
            return -1
        board[int( y )][x] = player

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

    def game_loop_ai(self):

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
                    self.player_click( posx, self.board, self.player )
                    self.bd.draw_board( self.board, self.player )
                    if self.win( self.player ) == self.player:
                        self.bd.print_board( self.board )
                        print( "player wins" )
                        time.sleep( 10 )
                        sys.exit()

                    print( "ai's turn" )
                    self.ai_move()
                    self.bd.draw_board( self.board, self.player )
                    if self.win( self.ai ) == self.ai:
                        self.bd.print_board( self.board )
                        print( "AI wins" )
                        time.sleep( 10 )
                        sys.exit()
                    self.bd.print_board( self.board )

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
                                        self.player = 1
                                        self.ai = 2
                                        self.game_loop_ai()
                                    else:
                                        self.gamemode = 1
                                        self.player = 2
                                        self.ai = 1
                                        self.game_loop_ai()
                    else:
                        self.gamemode = 1
                        self.game_loop()
