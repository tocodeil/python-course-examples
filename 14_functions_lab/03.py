"""
Write a function called "sum_tens" that calculates the sum
of the 10th digit from all arguments passed to it
"""


def sum_tens(*args):
	summery = 0
	for n in args:
		if type(n) is int: 
			summery += int(str(n)[-2:-1]) 
	return summery


#print sum_tens(120, 140, 1123)