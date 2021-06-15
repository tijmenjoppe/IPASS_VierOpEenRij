import random
import math
import numpy as np



class minimax:

    def __init__(self):
        self.game_over = None

    def minimax(self, position, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or self.game_over == True:
            return position

        if maximizingPlayer:
            maxEval = -math.inf
            for option in position:
                eval = self.minimax(option, depth - 1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = math.inf
            for option in position:
                eval = self.minimax( option, depth - 1, alpha, beta, True )
                minEval = min( minEval, eval )
                beta = min( beta, eval )
                if beta <= alpha:
                    break
            return minEval

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

    def evaluate_position(self, board):
        pass

    def score_position(self, row):
        score = 0
        if row.count() == 4:
            score += math.inf