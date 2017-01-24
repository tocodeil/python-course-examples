"""
Write a program that generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""
from random import randint

number = 0
while True:
    random_num = randint(1, 1000000)
    if random_num % 15 == 0:
        if random_num % 13 == 0:
            if random_num % 7 == 0:
                number = random_num
                break

print "The number %d is divisible by: 7, 13, and 15" % number
