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
import sys

if len(sys.argv) > 1:
    iteration = sys.argv[1]
    print ('Hello Python\n' * int(iteration))
else:
    program_name = sys.argv[0]
    print "Usage: %s <number of iterations>" % program_name