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
            currentgame.winner()
            #print "Next round:", counter
            rx = int(raw_input("Row: "))
            cx = int(raw_input("Column: "))

            currentgame.play(rx,cx)

            if currentgame.val(rx, cx) == True:
                currentgame.boardmarks[rx][cx] = [currentgame.current_player.mark]
                print currentgame.boardmarks[0][0], "|", currentgame.boardmarks[0][1], "|", currentgame.boardmarks[0][2]
                print "-----------------"
                print currentgame.boardmarks[1][0], "|", currentgame.boardmarks[1][1], "|", currentgame.boardmarks[1][2]
                print "-----------------"
                print currentgame.boardmarks[2][0], "|", currentgame.boardmarks[2][1], "|", currentgame.boardmarks[2][2]
                #print currentgame.boardmarks
                currentgame.swap_turn()
            else:
                raise InvalidMove("The place you chose is taken")

            counter = counter + 1

        except InvalidMove as e:
           print e
        except ValueError as e:
            print "you may only use numbers to indicate rows and colums"

    else:
        print "The game ended in a tie :("