from itertools import cycle

class InvalidMove(Exception): pass

class Game(object):
    boardmarks =  [[[''], [''], ['']], [[''], [''], ['']], [[''], [''], ['']]]

    def __init__(self):
        #boardmarks = [[[''], [''], ['']], [[''], [''], ['']], [[''], [''], ['']]]
        self.clearBoard()
        #self.winner() == False
        self.welcome_message()




    def start(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.players = cycle([p1, p2])
        self.current_player = self.players.next()
        #counter: count 8 game rounds. if no winner --> it's a tie 
        counter = 0

        self.clearBoard()

        pass

    def play(self, row, column):
        if row < 0 or row > 3 or column < 0 or column > 3:
            raise InvalidMove("You have made an illegal move! Please choose a number between 1-3")

        #availability testavail(row,column)

        #counter = counter + 1
        pass

    #@classmethod
    def winner():
        win = False
        #Check fow winner in each row --> 123 | 456 | 789 (+ mechanism for false winning if empty)
        if (Game.boardmarks[0][0] == Game.boardmarks[0][1]) and (Game.boardmarks[0][2] == Game.boardmarks[0][1]) and (Game.boardmarks[0][0] != ''):
            win = True
            print "Win 1"
        if (Game.boardmarks[1][0] == Game.boardmarks[1][1]) and (Game.boardmarks[1][2] == Game.boardmarks[1][1]) and (Game.boardmarks[1][0] != ''):
            win = True
            print "Win 2"
        if (Game.boardmarks[2][0] == Game.boardmarks[2][1]) and (Game.boardmarks[2][2] == Game.boardmarks[2][1]) and (Game.boardmarks[2][0] != ''):
            win = True
            print "Win 3"
        # Check fow winner in each column --> 147 | 258 | 369 (+ mechanism for false winning if empty)
        if (Game.boardmarks[0][0] == Game.boardmarks[1][0]) and (Game.boardmarks[2][0] == Game.boardmarks[1][0]) and (Game.boardmarks[0][0] != ''):
            win = True
            print "Win 4"
        if (Game.boardmarks[0][1] == Game.boardmarks[1][1]) and (Game.boardmarks[2][1] == Game.boardmarks[1][1]) and (Game.boardmarks[0][1] != ''):
            win = True
            print "Win 5"
        if (Game.boardmarks[0][2] == Game.boardmarks[1][2]) and (Game.boardmarks[2][2] == Game.boardmarks[1][2]) and (Game.boardmarks[0][2] != ''):
            win = True
            print "Win 6"
        # Check fow winner in diagonal --> 159 | 357 (+ mechanism for false winning if empty)
        if (Game.boardmarks[0][0] == Game.boardmarks[1][1]) and (Game.boardmarks[2][2] == Game.boardmarks[1][1]) and (Game.boardmarks[0][0] != ''):
            win = True
            print "Win 7"
        if (Game.boardmarks[0][2] == Game.boardmarks[1][1]) and (Game.boardmarks[2][0] == Game.boardmarks[1][1]) and (Game.boardmarks[0][2] != ''):
            win = True
            print "Win 8"
        return win


    def val(self, row, column):
        occupy = self.data[row][column]
        if not occupy:
            return False
        else:
            return occupy.val


    def clearBoard(self):
        self.boardmarks = [[[''], [''], ['']], [[''], [''], ['']], [[''], [''], ['']]]

    def welcome_message(self):
        print '***********************'
        print 'Welcome to Tic Tac Toe!'
        print '***********************'
        print 'This game was created for 2 players.'
        print 'Please enter your desired move in turns in the following format: row,column'
        print 'For example to mark the top right square, enter: \'1,3\'\n'
