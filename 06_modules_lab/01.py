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

if len(sys.argv) != 2 :
	print ("Usage: %s <number>" % sys.argv[0])
	sys.exit(1)
	
number = int(sys.argv[1])
for _ in range(number):
	print("Hello Python")
	
