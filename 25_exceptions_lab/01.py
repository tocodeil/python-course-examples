#!/usr/bin/python
from math import sqrt 
while True:
	num = raw_input()
	try:
		print sqrt(int(num))
	except ValueError as e:
		if num < 0:
			print ('num less then 0')
		else:
			print "Type only Numbers"