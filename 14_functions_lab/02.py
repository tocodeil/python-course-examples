#!/usr/bin/python
def take2(var1, var2):
		if type(var1) is str or type(var1) is int:
			if type(var2) is str or type(var2) is int:
				return var1, var2 
		else:
			raise ValueError


