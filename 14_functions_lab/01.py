import unittest
import numbers
"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""

def mysum(*args):
    num = [a for a in args if isinstance(a, numbers.Number)]
    sums = reduce(
        lambda a, b: a+b,
        num
    )
    return sums

def mymul(*args):
    num = [a for a in args if isinstance(a, numbers.Number)]
    sums = reduce(
        lambda a, b: a*b,
        num
    )
    return sums
