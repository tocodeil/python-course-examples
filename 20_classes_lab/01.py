"""
Write a class called "Summer" that provides the methods:
    add(n) - adds a number n to the sum
    total() - returns total sum of numbers added so far
"""

class Summer(object):
      
    def __init__(self):
        self.numlist = []
        self.totalsum = 0
      
    def add(self,*numlist):
        for i in numlist:
            self.numlist.append(i)
    def total(self):
        self.totalsum = sum(self.numlist)
        return self.totalsum

s = Summer()
t = Summer()

s.add(10,20)
t.add(50)
s.add(30)

print t.total()
print s.total()