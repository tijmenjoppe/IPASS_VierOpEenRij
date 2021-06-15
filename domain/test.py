import numpy as np
board = np.zeros((6, 7))
board[0][0] = 1
board[0][1] = 1
print(board)

def loop(board):
    lst_options = []

    for y in range(6):
        for x in range(6,-1,-1):
            if board[y][x] == 0.0:
                tuplexy = x, y
                lst_options.append(tuplexy)
                break
    return lst_options


def test_last_open_position(board, x):
    for y in range(5, -1, -1):
        if board[x][y] == 0.0:
            return y


def last_open_position(self, board, x):
    for index, row in enumerate(board):
        if row[x] == 0:
            return index
print(np.flip(board, 0))
print()
print(loop(board))
print(test_last_open_position(board, 0))

