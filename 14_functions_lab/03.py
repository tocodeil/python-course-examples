#!/usr/bin/python
def mydeciSum(*nums):
	return sum([int(x) for x in [str(x)[-2] for x in nums if len(str(x)) > 1 ]])
