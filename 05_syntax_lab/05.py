"""
Write a program that generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""

import random

while True:
    numbers = (random.randint(1, 1000000))
    x = numbers % 7
    y = numbers % 13
    z = numbers % 15
    if x == 0:
        if y == 0:
            if z == 0:
                print "The number " + str(numbers) + " divided 7, 13, 15"
                break


