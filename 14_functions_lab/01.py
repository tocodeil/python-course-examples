import unittest

"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""

def mysum(*args):
    total = 0
    for each in args:
        if type(each) == int:
            total += each
    return total

def mymul(start,*args):
    total = start
    for each in args:
        if type(each) == int:
            total = total * each
    return total
