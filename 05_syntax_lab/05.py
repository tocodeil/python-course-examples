
"""
Write a program that generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""
import random

while True:
    numbers = (random.randint(1, 1000000))

    if numbers % 7 and numbers % 13 and numbers % 15 == 0:
        print "Num " + str(numbers) + " is divided 7, 13, 15"
        exit()


