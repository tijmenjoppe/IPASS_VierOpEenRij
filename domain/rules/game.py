import math

import numpy as np

from domain.layout import board


class Game_Rules:

    def __init__(self):
        self.bd = board.Board()
        self.board = np.zeros( (6, 7) )
        self.player = 0
        self.gamemode = 0
        self.ai = 0
        self.game_turn = 0

    def win(self, player):
        b = self.board
        for i in range( 7 - 3 ):
            for j in range( 6 ):
                if b[j][i] == b[j][i + 1] and b[j][i + 1] == b[j][i + 2] and b[j][i + 2] == b[j][i + 3] and b[j][
                    i] == player:
                    return self.player

        for i in range( 7 ):
            for j in range( 6 - 3 ):
                if b[j][i] == b[j + 1][i] and b[j + 1][i] == b[j + 2][i] and b[j + 2][i] == b[j + 3][i] and b[j][
                    i] == player:
                    return self.player

        for i in range( 7 - 3 ):
            for j in range( 6 - 3 ):
                if b[j][i] == b[j + 1][i + 1] and b[j + 1][i + 1] == b[j + 2][i + 2] and b[j + 2][i + 2] == b[j + 3][
                    i + 3] and b[j][i] == player:
                    return self.player

        for i in range( 7 - 3 ):
            for j in range( 3, 6 ):
                if b[j][i] == b[j - 1][i + 1] and b[j - 1][i + 1] == b[j - 2][i + 2] and b[j - 2][i + 2] == b[j - 3][
                    i + 3] and b[j][i] == player:
                    return self.player

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

    def ai_move(self):
        move = self.minimax( self.board, 5, -math.inf, math.inf, True, self.ai, self.player )[1]
        self.move( self.ai, move[0], move[1], self.board )
        print( "AI move" )

    def terminal_node(self, board, player, ai):
        return self.win( player ) or self.win( ai ) or len( self.open_positions( board ) ) == 0

    def minimax(self, board, depth, alpha, beta, maximizingPlayer, ai, player):

        options = self.open_positions( board )

        if depth == 0 or self.terminal_node( board, player, ai ):
            return self.evaluate_position( board, ai )

        if maximizingPlayer:
            maxEval = -math.inf
            for option in options:
                board_copy = board.copy()
                self.move( ai, option[0], option[1], board_copy )
                eval = self.minimax( board_copy, depth - 1, alpha, beta, False, ai, player )[0]
                print( eval )
                maxEval = max( maxEval, eval )
                alpha = max( alpha, eval )
                if beta <= alpha:
                    break
            return maxEval, option

        else:
            minEval = math.inf
            for option in options:
                board_copy = board.copy()
                self.move( ai, option[0], option[1], board_copy )
                eval = self.minimax( board, depth - 1, alpha, beta, True, ai, player )[0]
                minEval = min( minEval, eval )
                beta = min( beta, eval )
                if beta <= alpha:
                    break
            return minEval, option

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
        opponent = (player + 1) % 2

        if lst.count( player ) == 4:
            score += math.inf
        elif lst.count( player ) == 3 and lst.count( 0 ) == 1:
            score += 900
        elif lst.count( player ) == 2 and lst.count( 0 ) == 2:
            score += 500
        elif lst.count( player ) == 1 and lst.count( 0 ) == 3:
            score += 300
        elif lst.count( player ) == 1 and lst.count( 0 ) == 2:
            score += 200
        if lst.count( opponent ) == 3 and lst.count( 0 ) == 1:
            score -= 900
        if lst.count( opponent ) == 4:
            score -= math.inf
