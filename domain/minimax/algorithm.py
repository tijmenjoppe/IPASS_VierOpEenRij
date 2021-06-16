import random
import math
import numpy as np
import domain.game as game




class minimax:

    def __init__(self):
        self.game_over = None
        self.gm = game.Game()

    def move(self, player, x, y, board):
        if y == None:
            return -1
        board[int(y)][x] = player

    def terminal_node(self, board, player, ai):
        return self.gm.win(player) or self.gm.win(ai) or len(self.open_positions(board)) == 0

    def minimax(self, board, depth, alpha, beta, maximizingPlayer, ai, player):

        options = self.open_positions(board)

        if depth == 0 or self.terminal_node(board, player, ai):
            return self.evaluate_position(board, ai)

        if maximizingPlayer:
            maxEval = -math.inf
            for option in options:
                board_copy = board.copy()
                self.move(ai, option[0], option[1], board_copy)
                eval = self.minimax(board_copy, depth - 1, alpha, beta, False, ai)[0]
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval, option

        else:
            minEval = math.inf
            for option in options:
                board_copy = board.copy()
                self.move( ai, option[0], option[1], board_copy )
                eval = self.minimax(board, depth - 1, alpha, beta, True, ai)[0]
                minEval = min( minEval, eval )
                beta = min( beta, eval )
                if beta <= alpha:
                    break
            return minEval, option

    def choice(self, options):
        return random.choice(options)

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
                lst = [b[j][i], b[j][i + 1],b[j][i + 2],b[j][i + 3]]
                score += self.score_position(lst,player)

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
                lst =  [b[j][i], b[j - 1][i + 1], b[j - 2][i + 2], b[j - 3][i + 3]]
                score += self.score_position(lst, player)

        return score

    def score_position(self, lst, player):
        score = 0
        opponent = (player + 1) % 2

        if lst.count( player ) == 4:
            score += math.inf
        elif lst.count( player ) == 3 and lst.count( 0 ) == 1:
            score += 90000
        elif lst.count( player ) == 2 and lst.count( 0 ) == 2:
            score += 50000
        elif lst.count( player ) == 1 and lst.count( 0 ) == 3:
            score += 30000
        elif lst.count( player ) == 1 and lst.count( 0 ) == 2:
            score += 20000
        if lst.count( opponent ) == 3 and lst.count( 0 ) == 1:
            score -= math.inf

        return score