import math
import random

import numpy as np

from domain.layout import board


class Game_Rules:
    ''' this class is used to play the game on a numpy matrix with player input and ai algorithm'''
    def __init__(self):
        self.bd = board.Board()
        self.board = np.zeros( (6, 7) )
        self.player = 0
        self.gamemode = 0
        self.ai = 0
        self.game_turn = 0

    def ai_move(self):
        ''' call the minimax algorithm to make a move'''
        move = self.minimax( self.board, 5, -math.inf, math.inf, True, self.ai, self.player )[1]
        if self.move( self.ai, move[0], move[1], self.board ) is None:
            return -1
        else:
            self.move( self.ai, move[0], move[1], self.board )
        print( "AI move" )

    def minimax(self, board, depth, alpha, beta, maximizingPlayer, ai, player):
        ''' minimax algorithm used to recursively find the best possible move'''
        options = self.open_positions( board )

        if depth == 0 or self.terminal_node( board, player, ai ):
            if self.terminal_node( board, player, ai ):
                if self.win( player ) == player:
                    return -math.inf, options
                if self.win( ai ) == ai:
                    return math.inf , options
            return self.evaluate_position( board, ai ), options

        if maximizingPlayer:
            maxEval = -math.inf
            bestOption = None
            for option in options:
                board_copy = board.copy()
                self.move( ai, option[0], option[1], board_copy )
                evalresult = self.minimax( board_copy, depth - 1, alpha, beta, False, ai, player )[0]
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
                if evalresult < minEval:
                    minEval = evalresult
                    worstOption = option
                minEval = min( minEval, evalresult )
                beta = min( beta, evalresult )
                if beta <= alpha:
                    break
            return minEval, worstOption

    def terminal_node(self, board, player, ai):
        ''' Function to look if the current 'node' is the last or terminal node'''
        return self.win( player ) or self.win( ai ) or len( self.open_positions( board ) ) == 0

    def open_positions(self, board):
        ''' look for all possible moves left'''
        lst_options = []

        for x in range( 7 ):
            for y in range( 5, -1, -1 ):
                if board[y][x] == 0.0:
                    tuplexy = x, y
                    lst_options.append( tuplexy )
                    break
        return lst_options

    def evaluate_position(self, board, player):
        ''' evaluate the state of the board by making short lists of four and evaluating those lists. similiar to looking for a win.'''
        score = 0
        b = board

        middle = [int( i ) for i in list( board[:, 7 // 2] )]
        middle_amount = middle.count( player )
        score += 200 * middle_amount

        for i in range( 7 - 3 ):
            for j in range( 6 ):
                lst = [b[j][i], b[j][i + 1], b[j][i + 2], b[j][i + 3]]
                score += self.score_position(lst, player)

        for i in range( 7 ):
            for j in range( 6 - 3 ):
                lst = [b[j][i], b[j + 1][i], b[j + 2][i], b[j + 3][i]]
                score += self.score_position(lst, player)

        for i in range( 7 - 3 ):
            for j in range( 6 - 3 ):
                lst = [b[j][i], b[j + 1][i + 1], b[j + 2][i + 2], b[j + 3][i + 3]]
                score += self.score_position(lst, player)

        for i in range( 7 - 3 ):
            for j in range( 3, 6 ):
                lst = [b[j][i], b[j - 1][i + 1], b[j - 2][i + 2], b[j - 3][i + 3]]
                score += self.score_position( lst, player )

        return score

    def score_position(self, lst, player):
        ''' after a list of four spaces is created you will look how many AI or player pieces there are in that list or open spaces. and give an evaluation based upon a set of rules'''
        score = 0
        opponent = self.player

        if lst.count( player ) == 4:
            score += math.inf
        if lst.count( player ) == 3 and lst.count( 0 ) == 1:
            score += 900
        if lst.count( player ) == 2 and lst.count( 0 ) == 2:
            score += 400
        if lst.count( opponent ) == 2 and lst.count( 0 ) == 2:
            score -= 400
        if lst.count( opponent ) == 3 and lst.count( 0 ) == 1:
            score -= 900
        if lst.count( opponent ) == 4:
            score -= math.inf

        return score

    def choice(self, options):
        ''' make a random choice in a list of possible moves'''
        return random.choice( options )

    def win(self, player):
        ''' look for a win in the board, by looping through and checking if anywhere on the board there is a row or column or diagonal where four pieces are aligned'''
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
        ''' if a player clicks on the screen get its X and Y coordinates so you can place a piece where the player intended'''
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
        ''' find the last open position in a column so you can drop the piece to the bottom of the board'''
        for y in range( 5, -1, -1 ):
            if board[y][x] == 0.0:
                return y

    def move(self, player, x, y, board):
        ''' place a piece on the numpy matrix given the X and Y'''
        if y == None:
            return -1
        board[int( y )][x] = player