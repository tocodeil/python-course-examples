""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
"""

import sys

if len(sys.argv) != 3:
	print "Usage: %s <number1> <number2> " %sys.argv[0]
	sys.exit(1)
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print "The sum is:" ,num1 + num2