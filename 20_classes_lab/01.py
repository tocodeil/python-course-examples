"""
Write a class called "Summer" that provides the methods:
    add(n) - adds a number n to the sum
    total() - returns total sum of numbers added so far
"""

class Summer(object):
    def __init__(self):
        self._total = 0

    def add(self, *numbers):
        self._total += sum(numbers)

    def total(self):
        return self._total

s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

print s.total()
print t.total()