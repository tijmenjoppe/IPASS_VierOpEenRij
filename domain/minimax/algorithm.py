


class minimax:

    def __init__(self):
        self.game_over = None

    def minimax(self, position, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or self.game_over == True:
            return position

        if maximizingPlayer:
            maxEval = -100000
            for option in position:
                eval = self.minimax(option, depth - 1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = 100000
            for option in position:
                eval = self.minimax( option, depth - 1, alpha, beta, True )
                minEval = min( minEval, eval )
                beta = min( beta, eval )
                if beta <= alpha:
                    break
            return minEval
