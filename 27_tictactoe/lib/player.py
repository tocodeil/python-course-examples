"""
player implementation
"""

class InvalidPlayerTag(Exception): pass

class Player(object):
    def __init__(self, name, tag):
        self._name = name
        if tag != 'X' and tag != 'O':
            raise InvalidPlayerTag("Player tag value should be either X or O")
        self._tag = tag

    def __eq__(self,other):
        if isinstance(other, Player):
            return self._name == other._name and self._tag == other._tag
        else:
            return NotImplemented
