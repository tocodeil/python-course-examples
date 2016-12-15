"""
Write a program that generates 2 random numbers
and calculates their least common multiple,
that is the smallest number that is divisible
by both.
For example if the numbers were 4 and 6,
program should print 12.
"""

import random
x = random.randint(1,10)
y = random.randint(1,10)


# make sure that x is the bigger number
if x < y :
	c = x
	x = y
	y = c

c = x	
print x, y 



if (c % x == 0 and c % y == 0):
	print "The number is", c


else :
	helper = 0
	while helper != 1:
		c +=  1
		if (c % x == 0 and c % y == 0):
			print "The number is", c
			helper = 1
	




