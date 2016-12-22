class Player(object):
    """build a player. receive from the user a name and side (O or X)"""
    name = ''
    mark = ''

    def __init__(self, n1, m1):
        self.name = n1
        self.mark = m1

