import numpy as np
from domain.rules import game_loops
import numpy as np
from domain.rules import game

board = np.zeros( (6, 7) )

player = 1
ai = 2

gm = game.Game_Rules()

gm.player = 1
gm.ai = 2
def function_test_open_positions():
    print('''the function open_positions looks for all possible moves for the AI. In an empty board you asume its 7 moves the computer can make''')
    print('is the length of the list of open positions 7?')
    print( len(gm.open_positions( board )) == 7 )
    print(''' if we fill a column there should only be six possible moves''')
    print('Here we test the Move function that will place a piece if you give its coordinates')
    print('I loop through and add 1 on the y')
    for i in range(6):
        gm.move(player, 0, i, board)
        print(board)
    print('as you can see one column of the board is now filled.')
    print('is the length of the list of open positions still 7?')
    print( len(gm.open_positions( board )) == 7 )


def function_test_evaluate_position():
    board = np.zeros( (6, 7))
    print('This function will evaluate a board state')
    print(" I am going to place an piece in the middle, for its a strong position to hold.")
    print("the calculation is for every piece in the middle from the AI you get 200 points")
    gm.move(ai, 3, 5, board)
    print(board)
    print(" is the score of the positions 200?")
    print(gm.evaluate_position(board, ai) ==  200)

function_test_open_positions()
function_test_evaluate_position()