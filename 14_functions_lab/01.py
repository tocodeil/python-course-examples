import unittest

"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""
import sys

def mysum(*numbers):
    res = 0.0
    for number in numbers:
        if type(number) == type(1):
            res = res + number
        if type(number) == type(1.0):
            res = res + number
    return res

def mymul(*numbers):
    res = 1.0
    for number in numbers:
        if type(number) == type(1):
            res = res * number
        if type(number) == type(1.0):
            res = res * number
    return res
