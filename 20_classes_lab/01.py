"""
Write a class called "Summer" that provides the methods:
    add(n) - adds a number n to the sum
    total() - returns total sum of numbers added so far
"""
class Summer(object):
    def __init__(self):
        self._sum = 0

    def add(self,*values):
        for value in values:
            self._sum += value
    
    def total(self):
        return self._sum
