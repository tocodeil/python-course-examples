
class Summer(object):
    def __init__(self):
        self.number = 0

    def add(self, *args):
        for n in args:
            self.number += n

    def total(self):
        return self.number


s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
print s.total()

# should print 50
print t.total()