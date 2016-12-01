""" The program takes a count
from sys.argv import and prints "Hello Python"
count times.

"""
import sys

num = int(sys.argv[1])
while num != 0:
	print "Hello Python"
	num -= 1