import numpy as np
from domain.rules import game
import unittest


class TestStringMethods( unittest.TestCase ):

    def test_function_test_open_positions(self):
        self.board = np.zeros( (6, 7) )
        self.player = 1
        self.ai = 2
        self.gm = game.Game_Rules()
        self.gm.player = 1
        self.gm.ai = 2
        """ the function open_positions looks for all possible moves for the AI. In an empty board you assume its 7
        moves the computer can make  is the length of the list of open positions 7? """
        self.assertEqual( len( self.gm.open_positions( self.board ) ), 7 )
        """ if we fill a column there should only be six possible moves Here we test the Move function that will place 
        a piece if you give its coordinates I loop through and add 1 on the y """
        for i in range( 6 ):
            self.gm.move( self.player, 0, i, self.board )
            print( self.board )
        '''as you can see one column of the board is now filled.
        is the length of the list of open positions 6?'''
        self.assertEqual( len( self.gm.open_positions( self.board ) ), 6 )

    def test_function_test_evaluate_position(self):
        self.board = np.zeros( (6, 7) )
        self.player = 1
        self.ai = 2
        self.gm = game.Game_Rules()
        self.gm.player = 1
        self.gm.ai = 2
        self.board = np.zeros( (6, 7) )
        '''This function will evaluate a board state
        I am going to place an piece in the middle, for its a strong position to hold.
        the calculation is for every piece in the middle from the AI you get 200 points'''
        self.gm.move( self.ai, 3, 5, self.board )
        print( self.board )
        '''is the score of the positions 200?'''
        self.assertEqual( self.gm.evaluate_position( self.board, self.ai ), 200 )


if __name__ == '__main__':
    unittest.main()
