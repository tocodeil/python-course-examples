#!/usr/bin/python
class Summer(object):
	def __init__(self):
		self.x = 0
	def add(self,*args):
		self.x +=  sum([int(arg) for arg in args])
	def total(self):
		return self.x	

s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
print s.total()

# should print 50
print t.total()