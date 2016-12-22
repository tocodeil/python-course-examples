"""
board implementation
"""
from lib.player import Player

class InvalidPlayersType(Exception): pass

class InvalidMove(Exception): pass


class board(object):

    def __init__(self):
        self._player1 = None
        self._player2 = None
        self.current_player = None
        self.data = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self._winner = None

    @classmethod
    def Game(cls):
        return board()
    
    def start(self,player1,player2):
        if type(player1) == Player and type(player2) == Player:
            self._player1 = player1
            self._player2 = player2
            self.current_player = player1
            self.data = [
                [None, None, None],
                [None, None, None],
                [None, None, None],
            ]
            self._winner = None
        else:
            raise InvalidPlayersType("start method should get parameters of type player")

    def play(self, row, column):
        if type(row) != int or type(column) != int:
            raise InvalidMove("row and column values should be integers")
        if row < 0 or row > 2 or column < 0 or column > 2:
            raise InvalidMove("square should be inside 3X3 board. columns and rows values should be between 0-2")
        if self.gameisover() == True:
            raise InvalidMove("Game is already over")
        if self.data[row][column] != None:
            raise InvalidMove("square (%d,%d) is already taken" % (row,column))
        self.data[row][column] = self.current_player
        if self._player1 == self.current_player:
            self.current_player = self._player2
        else:
            self.current_player = self._player1

    def checkwinner(self):
        for i in range(3):
            if self.data[i][0] != None:
                if self.data[i][0] == self.data[i][1] and self.data[i][0] == self.data[i][2]:
                    self._winner = self.data[i][0]
                    return self._winner
        for j in range(3):
            if self.data[0][j] != None:
                if self.data[0][j] == self.data[1][j] and self.data[0][j] == self.data[2][j]:
                    self._winner = self.data[0][j]
                    return self._winner
        if self.data[0][0] != None:
            if self.data[0][0] == self.data[1][1] and self.data[0][0] == self.data[2][2]:
                self._winner = self.data[0][0]
                return self._winner
        if self.data[0][2] != None:
            if self.data[0][2] == self.data[1][1] and self.data[0][2] == self.data[2][0]:
                self._winner = self.data[0][2]
                return self._winner
        self._winner = None
        return self._winner

    def tie(self):
        if self.checkwinner() != None:
            return False
        for i in range(3):
            for j in range(3):
                if self.data[i][j] == None:
                    return False
        return True

    def gameisover(self):
        if self.checkwinner() != None:
            return True
        return self.tie()

    def winner(self):
        if self.gameisover() == True:
            return self.checkwinner()
        return None

    def val(self, row, column):
        if self.data[row][column] == None:
            return "None"
        return self.data[row][column]._tag