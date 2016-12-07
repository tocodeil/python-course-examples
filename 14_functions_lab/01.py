import unittest

"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""


def mysum(*numbers):
    res = 0
    for n in numbers:
        if type(n) is int:
            res += n
    return res

def mymul(*numbers):
    res = 1
    for n in numbers:
        if type(n) is int:
            res *= n
    return res
    

#print sum(1,2,'2',"foo")
#print multi(4,2,'2',"foo")