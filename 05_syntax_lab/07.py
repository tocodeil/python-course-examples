""" Write a program that selects a random number
and asks the user to guess it.
After each guess print a hint "too large" or "too small" to the user.
Bonus: To make things interesting, the program should cheat once in a white
"""

from random import randint

num2Guess = randint(1,100)

print("Guess a number!")

guess = int(raw_input())
fountit = False
while not fountIt:
	if guess > num2Guess:
		print("too large")
		guess = int(raw_input())
	elif guess < num2Guess:
		print("too small")
		guess = int(raw_input())
	elif guess == num2Guess:
		print("found it!")
		fountit = True
