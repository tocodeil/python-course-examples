""" Main project file
"""
import lib.board as board
from lib.player import Player

def print_board():
    for row in range(3):
        for col in range(3):
            print g.val(row, col),
        print "\n"


p1 = Player(raw_input("player 1 name: "), "X")
p2 = Player(raw_input("player 2 name: "), "O")

g = board.Game()
g.start(p1, p2)

while True:
    print_board()

    (winner, tie) = g.checkwinner()

    if winner != None:
        print "%s wins!!!" % g.winner.name
        break

    if tie: # don't call tie() - there is no need to checkwinner again
        print "tie"
        break
    

    try: 
        (x,y) = [int(n) for n in raw_input("%s play: " % g.current_player.name).split()]        
        g.play(x,y)
    
    except ValueError:
        print "Invalid input"

    except board.InvalidMove:
        print "Invalid move"


