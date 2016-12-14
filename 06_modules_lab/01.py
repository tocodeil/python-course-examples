""" Write a program that takes a count
from sys.argv import and prints "Hello Python"
count times.

For example if program was started as:
    python 01.py 5

It should print:
    Hello Python
    Hello Python
    Hello Python
    Hello Python
    Hello Python
"""
x = 0

import sys

y = sys.argv[1]

y = int(sys.argv[1])

while x <= y :
    print "Hellow Python"
    x = x + 1


