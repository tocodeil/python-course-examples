"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""
sum=0
from random import randint
for i in range(1, 8):

    numbers = randint(1,100)
    sum+=numbers

print sum
