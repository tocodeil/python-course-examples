""" 
Write a program that takes a count
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

(_, count) = sys.argv

for _ in range(0, int(count)):
    print "Hello Python"

