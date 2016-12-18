
class InvalidMove(Exception):
    pass

class Game(object):
    def __init__(self):
        pass

    def start(self, p1, p2):
        self.winner = None
        self.current_player = p1
        self.other_player = p2
        self.data = [[None for x in range(3)] for x in range(3)]


    def play(self, row, column):
        if row not in range(3) or column not in range(3):
            raise InvalidMove


        if self.data[row][column] != None:
            raise InvalidMove

        self.data[row][column] = self.current_player

        # switch players:
        temp = self.current_player
        self.current_player = self.other_player
        self.other_player = temp

    def val(self, row, column):
        player = self.data[row][column]
        if player == None:
            return '-'
        else:
            return player.char 

    def _checkwinnervalues(self, a,b,c):
        if a == b and b == c and a != None:
            self.winner = a
            self._tie = False
            return True
        else:
            # if we have at least 2 empty values in this line or 2 values of same player and the 3rd is empty - this is not a tie
            if a == b and (c == None or a == None) or c == b and (a == None or c == None):
                self._tie = False
            return False 

    # return the winner if any and if this is a tie: (winner, tie)
    def checkwinner(self):
        self._tie = True

        # check rows:        
        for row in range(3):
            if self._checkwinnervalues(self.data[row][0], self.data[row][1], self.data[row][2]):                
                return (self.winner, False)
        
        # check columnes:
        for col in range(3):
            if self._checkwinnervalues(self.data[0][col], self.data[1][col], self.data[2][col]):
                return (self.winner, False)
        
        #check diags
        if self._checkwinnervalues(self.data[0][0], self.data[1][1], self.data[2][2]):
            return (self.winner, False)

        if self._checkwinnervalues(self.data[2][0], self.data[1][1], self.data[0][2]):
            return (self.winner, False)

        return (None, self._tie)

    def tie(self):
        (winner, tie) = self.checkwinner()
        return tie
