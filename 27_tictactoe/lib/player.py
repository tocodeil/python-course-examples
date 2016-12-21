class Player(object):
    """build a player. receive from the user a name and side (O or X)"""
    name = ''
    side = ''

    def __init__(self, name, mark):
        self.n = name
        self.m = mark

