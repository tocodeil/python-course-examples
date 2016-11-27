"""
Write a program that generates a random number
between 1 and 10,000,
and prints the sum of its digits.
For example if the number was: 2345
the result should be: 14.
"""
from random import randint

number = randint(1,10000)

sum = 0
for digit in str(number):
	sum += int(digit)

print sum
