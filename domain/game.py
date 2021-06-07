''' combineer board en rules om het spel werkend te maken zodat je tegen jezelf kan spelen'''
from layout import board
from layout import rules
import pygame as pg
import sys
from pygame.locals import *

class Game:

    def __init__(self):
        self.bd = board.Board()
        self.rl = rules.Rules()


    def connect_four_game(self):

        self.bd.first_screen()


        while True:

            self.bd.create_canvas().convert()

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONUP:
                    self.rl.printMouseCoordinates(pg.mouse.get_pos())

