"""
Write a class called "Summer" that provides the methods:
    add(n) - adds a number n to the sum
    total() - returns total sum of numbers added so far
"""


class Summer(object):
	def __init__(self):
		self.items = []
	def add(self,item,item1 = 0):
		self.items +=[item,item1]
	def total(self):
		return sum([int (i) for i in self.items])
		

s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
print s.total()

# should print 50
print t.total()