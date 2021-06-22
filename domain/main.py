import pygame as pg
import sys
from pygame.locals import *


from domain import game_loops

connect_game = game_loops.Game_Loops()
''' here we call the game loop function'''
connect_game.connect_four_game()

