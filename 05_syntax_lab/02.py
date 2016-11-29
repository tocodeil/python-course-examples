"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""

from random import randint

s = 0
print "Random 7 integers:",
for _ in range(7):
    n = randint(1, 100)
    s = s + n
    print " %d" % n,
print
print "Sum of numbers: %d" % s

if s % 7 == 0:
    print "Boom"