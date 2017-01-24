""" Write a program that selects a random number
and asks the user to guess it.
After each guess print a hint "too large" or "too small" to the user.
Bonus: To make things interesting, the program should cheat once in a white
"""

import random

prints = ['too small', 'too large']
randomNumber = random.randint(0,100)
print ("Please guesss the number between 0 and 100:")
while True:
	guess = int(raw_input())
	if (guess == randomNumber):
		break
	elif ((guess % 2 == 0) and (guess % 14 == 0)): # might cheat if the guess was %2==0 and %14==0 like 14, 28, 42....
		print(random.choice (prints))	
	elif(guess < randomNumber):
		print(prints[0])
		#print("too small")
	else:
		print(prints[1])
		#print("too large")

print ("You guessed correctly! the number was: {randomNumber}".format(randomNumber=randomNumber))