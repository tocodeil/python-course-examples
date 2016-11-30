"""
Write a program that generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""
from random import randint

found = False

while(found != True):
    num = randint(1,1000000)
    if((num % 7 == 0) and (num % 13 == 0) and (num % 15 == 0)):
        found = True

print "num",num