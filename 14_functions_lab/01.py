import unittest

"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""

def mysum(*numbers):
    the_sum = 0
    for number in numbers:
        if type(number) == int or type(number) == float:
            the_sum += number
    return the_sum


def mymul(*numbers):
    # if you multiply a number by zero, you'll get a zero
    the_sum = 1
    for number in numbers:
        if type(number) == int or type(number) == float:
            the_sum *= number
    return the_sum


print(mysum(1, 2, 3, 'boo', 'blah'))
print(mymul(2, 3, 3, 'boo'))