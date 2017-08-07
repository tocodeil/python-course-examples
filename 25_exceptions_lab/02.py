#!/usr/bin/python
import sys
try:
	with open(sys.argv[1] ,'r') as f:
		print len(f)
except IOError as e:
	print 'sorry file %s , not found' % sys.argv[1]