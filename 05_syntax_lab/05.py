"""
Write a program that generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""

import random
import sys

number = 0
while True:
	number = random.randint(0, sys.maxint)
	if (number % 7 == 0) and (number % 13 == 0) and (number % 15 == 0):
		break
print (number)