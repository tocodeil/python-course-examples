"""
Write a program that generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""

from random import randint

num = 1

while ( not ((num % 7 == 0) and (num % 13 == 0) and (num % 15 == 0))):
		num = randint(1,10000)

print("Found it: ", num)