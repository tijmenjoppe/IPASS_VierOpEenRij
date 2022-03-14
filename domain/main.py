import os
import sys

dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(f"Adding '{dir}' to the file path.")
sys.path.insert(0, dir)

from domain.rules import game_loops

connect_game = game_loops.Game_Loops()
''' here we call the game loop function'''
connect_game.connect_four_game()

