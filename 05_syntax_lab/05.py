"""
Write a program that generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""

from random import randint

while True:
	n = randint(1,1000000)
	if (n % 7 == 0 and n % 13 == 0 and n % 15 == 0):
		print n
		break;