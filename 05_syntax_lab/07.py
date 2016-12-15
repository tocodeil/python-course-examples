""" Write a program that selects a random number
and asks the user to guess it.
After each guess print a hint "too large" or "too small" to the user.
Bonus: To make things interesting, the program should cheat once in a white
"""


print "plase inset 3 numbers between 0 - 50 :"
#
x = float(raw_input())
import random
x_ = random.randint(0,50)
if x > x_:
	print "too big"

elif x < x_ :
	print "too small"
	
else :
		print "WOW"

#		
y = float(raw_input())
y_ = random.randint(0,50)
if y > y_:
	print "too big"

elif y < y_ :
	print "too small"
	
else :
	print "WOW"

#
z = float(raw_input())
z_ = random.randint(0,50)
if z > z_:
	print "too big"

elif z < z_ :
	print "too small"
	
else :
	print "WOW"
