from itertools import cycle


class InvalidMove(Exception):
    pass


class Game(object):
    boardmarks = [[[''], [''], ['']], [[''], [''], ['']], [[''], [''], ['']]]
    players = ''
    current_player = ''

    def __init__(self):
        self.clearBoard()
        #self.welcome_message()

    def start(self, pl1, pl2):
        self.p1 = pl1
        self.p2 = pl2
        self.players = cycle((self.p1, self.p2))
        self.current_player = self.players.next()
        print "Player turn: ", self.current_player.name

    def swap_turn(self):
        self.current_player = self.players.next()
        print "Player turn: ", self.current_player.name

    def play(self, row, column):
        if row < 0 or row > 2 or column < 0 or column > 2:
            raise InvalidMove("You have made an illegal move! Please choose a number between 1-3")

    def winner(self):
        #Check fow winner in each row --> 123 | 456 | 789 (+ mechanism for false winning if empty)
        if (self.boardmarks[0][0] == self.boardmarks[0][1]) and (self.boardmarks[0][2] == self.boardmarks[0][1]) and (self.boardmarks[0][0] != ['']):
            #print self.boardmarks[0][0], self.boardmarks[0][1], self.boardmarks[0][2]
            print "You Won!"
        elif (self.boardmarks[1][0] == self.boardmarks[1][1]) and (self.boardmarks[1][2] == self.boardmarks[1][1]) and (self.boardmarks[1][0] != ['']):
            print "You Won!"
        elif (self.boardmarks[2][0] == self.boardmarks[2][1]) and (self.boardmarks[2][2] == self.boardmarks[2][1]) and (self.boardmarks[2][0] != ['']):
            print "You Won!"
        # Check fow winner in each column --> 147 | 258 | 369 (+ mechanism for false winning if empty)
        elif (self.boardmarks[0][0] == self.boardmarks[1][0]) and (self.boardmarks[2][0] == self.boardmarks[1][0]) and (self.boardmarks[0][0] != ['']):
            print "You Won!"
        elif (self.boardmarks[0][1] == self.boardmarks[1][1]) and (self.boardmarks[2][1] == self.boardmarks[1][1]) and (self.boardmarks[0][1] != ['']):
            print "You Won!"
        elif (self.boardmarks[0][2] == self.boardmarks[1][2]) and (self.boardmarks[2][2] == self.boardmarks[1][2]) and (self.boardmarks[0][2] != ['']):
            print "You Won!"
        # Check fow winner in diagonal --> 159 | 357 (+ mechanism for false winning if empty)
        elif (self.boardmarks[0][0] == self.boardmarks[1][1]) and (self.boardmarks[2][2] == self.boardmarks[1][1]) and (self.boardmarks[0][0] != ['']):
            print "You Won!"
        elif (self.boardmarks[0][2] == self.boardmarks[1][1]) and (self.boardmarks[2][0] == self.boardmarks[1][1]) and (self.boardmarks[0][2] != ['']):
            print "You Won!"
        else:
            return None

    def val(self, row, column):
        if self.boardmarks[row][column] == ['']:
            #print "true"
            return True
        else:
            #print "false"
            return False

    def clearBoard(self):
        self.boardmarks = [[[''], [''], ['']], [[''], [''], ['']], [[''], [''], ['']]]

    def welcome_message(self):
        print '***********************'
        print 'Welcome to Tic Tac Toe!'
        print '***********************'
        print 'This game was created for 2 players.'
        print 'Please enter your desired move in turns in the following format: row,column'
        print 'For example to mark the top right square, enter: \'1,3\'\n'