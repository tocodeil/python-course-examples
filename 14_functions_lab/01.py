import unittest

"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""
#import type

def mysum(*args):
	sum = 0
	for n in args:
		if type(n) == int:
			sum += n
	return sum

def mymul(*args):
	mul = 1
	for n in args:
		if type(n) == int:
			mul *= n
	return mul


print mysum(8,0,3,'fff','fkfk')
print mymul('fgds','0','',17)