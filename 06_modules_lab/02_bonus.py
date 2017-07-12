#!/usr/bin/python

import sys
import os 
try:
	if len(sys.argv) != 3: 
		print 'Usage: %s <num 1> <num 2>' % sys.argv[0]
		sys.exit()
	else:
		print ( int(sys.argv[1]) , int (sys.argv[2]))		
except ValueError ,e:
	print 'one or more of the numbers are not convertiable to int'

print 333