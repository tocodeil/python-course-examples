"""
Write a program that generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""

import random


num = 1

while num % 7 != 0 or num % 13 != 0 or num % 15 != 0:
    num = random.randint(0, 1000000)

print num