""" Main project file
"""
import lib.board as board
import lib.player as player

def PrintTable(game):
    print "%10s%10s%10s" % (game.val(0,0), game.val(0,1), game.val(0,2)) 
    print "%10s%10s%10s" % (game.val(1,0), game.val(1,1), game.val(1,2))
    print "%10s%10s%10s" % (game.val(2,0), game.val(2,1), game.val(2,2))


while True:
    try:
        print "please enter name for first player"
        name1 = raw_input()
        print "please enter tag (X or O) for first player"
        tag1 = raw_input()
        p1 = player.Player(name1, tag1)
        tag2 = ""
        if tag1 == 'X':
            tag2 = 'O'
        else:
            tag2 = 'X'
        print "please enter name for second player"
        name2 = raw_input()
        print "tag for second player will be ", tag2
        p2 = player.Player(name2, tag2)
    except player.InvalidPlayerTag  as e:
        print e
        continue
    except BaseException  as e:
        print e
        continue
    break 

g = board.board.Game()

g.start(p1, p2)

while(g.gameisover() == False):
    try:
        print "%s plase select move row between 0-2" % g.current_player._name
        raw = int(raw_input())
        print "%s plase select move column between 0-2" % g.current_player._name
        column = int(raw_input())
        g.play(raw,column)
    except board.InvalidPlayersType  as e:
        print e
        continue
    except board.InvalidMove  as e:
        print e
        continue
    except BaseException  as e:
        print e
        continue
        
    PrintTable(g)
    

if g.tie() == True:
    print "The game ended with a tie between %s and %s" % (p1._name, p2._name)
else:
    print "And the winner is %s" % g.checkwinner()._name
PrintTable(g)