"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""

import random

sumOfNumbers = 0
for _ in range(7):
    sumOfNumbers += random.randint(1, 100)

print sumOfNumbers
if sumOfNumbers % 7 == 0:
    print "Boom"
