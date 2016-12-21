""" Main project file for Tic Tac Toe game
"""
#import lib.board as board
from lib.board import Game
from lib.board import InvalidMove
from lib.player import Player



if __name__ == "__main__":

    p1 = Player("Moshe", "X")
    p2 = Player("Oren", "O")
    counter = 0
    currentgame = Game()
    currentgame.start(p1, p2)

    while counter < 9:
        try:
            rx = int(raw_input("Row: "))
            cx = int(raw_input("Column: "))

            currentgame.play(rx,cx)
            if currentgame.winner():
                print "Congratulations! you won :)"
            else:
                continue
    # calling board with two players
            #currentgame.start(p1,p2)

        except InvalidMove as e:
           print e
        except ValueError as e:
            print "you may only use numbers to indicate rows and colums"