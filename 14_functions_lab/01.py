import unittest

"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""

def mysum(*args):
	return sum([x for x in args if isinstance(x, int)])
def mymul (*args):
	return reduce (
		lambda acc, val: acc * val,
		[x for x in args if isinstance(x, int)]
		)