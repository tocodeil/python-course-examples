"""
Write a program that generates 2 random numbers
and calculates their least common multiple,
that is the smallest number that is divisible
by both.
For example if the numbers were 4 and 6,
program should print 12.
"""

from random import randint

a = randint(1,10)
b = randint(1,10)

found = False
result = 0

while(found == False):
    result += 1
    found = (result % a == 0) and (result % b == 0)

print result  