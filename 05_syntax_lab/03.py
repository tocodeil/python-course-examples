"""
Write a program that generates a random number
between 1 and 10,000,
and prints the sum of its digits.
For example if the number was: 2345
the result should be: 14.
"""

from random import randint

random_number = str(randint(1, 10000))
#print "The random number is " + random_number
total_digits = 0

for digit in str(random_number):
    total_digits += int(digit)

print total_digits
total_digits = 0