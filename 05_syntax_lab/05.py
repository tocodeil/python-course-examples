"""
Write a program that generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""

from random import randint

while True:
    number = randint(1, 1000000)
    if number % 7 == 0 and number % 13 == 0 and number % 15 == 0:
        print "Bingo! The number that meets the criterion is " + str(number)
        break
