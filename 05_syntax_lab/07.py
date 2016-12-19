""" Write a program that selects a random number
and asks the user to guess it.
After each guess print a hint "too large" or "too small" to the user.
Bonus: To make things interesting, the program should cheat once in a white
"""


from random import randint
x = randint(1,100)

while True:
	guess = int(raw_input())

	if (guess == x):
		print "you guessed it!"
		break
	elif (guess > x):
		print "too large"
	else:
		print "too small"
