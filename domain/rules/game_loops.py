from domain.layout import board
from domain.rules import game
import pygame as pg
import sys
from pygame.locals import *
import time


class Game_Loops:

    def __init__(self):
        self.bd = board.Board()
        self.gm = game.Game_Rules()
        self.game_turn = 0

    def game_loop(self):
        ''' The game loop if you want to play against yourself or against another player.'''
        self.bd.gameDisplay.fill( self.bd.black )
        self.bd.draw_board( self.gm.board, self.gm.player )
        pg.display.update()
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    posx, posy = pg.mouse.get_pos()
                    if self.gm.player == 1:
                        # red
                        self.gm.player_click( posx, self.gm.board, self.gm.player )
                        self.bd.draw_board( self.gm.board, self.gm.player )
                        if self.gm.win( self.gm.player ) == 1:
                            print( "red wins" )
                            time.sleep( 10 )
                            sys.exit()
                    else:
                        # yellow
                        self.gm.player = 2
                        self.gm.player_click( posx, self.gm.board, self.gm.player )
                        self.bd.draw_board( self.gm.board, self.gm.player )
                        if self.gm.win( self.gm.player ) == 2:
                            print( "yellow wins" )
                            time.sleep( 10 )
                            sys.exit()
                    self.gm.player += 1
                    self.gm.player = self.gm.player % 2

    def game_loop_ai(self):
        ''' The game loop for when you decide to play against the AI'''
        self.bd.gameDisplay.fill( self.bd.black )
        self.bd.draw_board( self.gm.board, self.gm.player )
        pg.display.update()
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    posx, posy = pg.mouse.get_pos()
                    self.gm.player_click( posx, self.gm.board, self.gm.player )
                    self.bd.draw_board( self.gm.board, self.gm.player )
                    if self.gm.win( self.gm.player ) == self.gm.player:
                        print( "player wins" )
                        time.sleep( 10 )
                        sys.exit()

                    print( "ai's turn" )
                    self.gm.ai_move()
                    self.bd.draw_board( self.gm.board, self.gm.player )
                    if self.gm.win( self.gm.ai ) == self.gm.ai :
                        print( "AI wins" )
                        time.sleep( 10 )
                        sys.exit()
                    self.bd.draw_board( self.gm.board, self.gm.player )

    def connect_four_game(self):
        '''This is the game itself. you can choose one of the two game loops and play the game connect four'''
        pg.init()
        self.bd.first_screen()
        pg.display.update()
        self.bd.first_menu()
        pg.display.update()

        while self.gm.gamemode == 0:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    posx, posy = pg.mouse.get_pos()
                    if posx < 350:
                        self.bd.ai_menu()
                        while self.gm.gamemode == 0:
                            for event in pg.event.get():
                                if event.type == QUIT:
                                    pg.quit()
                                    sys.exit()
                                if event.type == pg.MOUSEBUTTONDOWN:
                                    posx, posy = pg.mouse.get_pos()
                                    if posx < 350:
                                        self.gm.gamemode = 1
                                        self.gm.player = 1
                                        self.gm.ai  = 2
                                        self.game_loop_ai()
                                    else:
                                        self.gm.gamemode = 1
                                        self.gm.player = 2
                                        self.gm.ai  = 1
                                        self.game_loop_ai()
                    else:
                        self.gm.gamemode = 1
                        self.game_loop()
