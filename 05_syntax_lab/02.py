"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""

from random import randint

sum = 0
for _ in range(7):
	num = randint(1,100)
	sum += num

print sum,
if sum % 7 == 0:
	print "Boom"