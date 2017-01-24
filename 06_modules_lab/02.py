""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
"""

import sys

if len(sys.argv) != 3 :
	print ("Usage: %s <firstNumber> <secondNumber>" % sys.argv[0])
	sys.exit(1)
	
firstNumber = int(sys.argv[1])
secondNumber = int(sys.argv[2])
print ("The sum of %d + %d is: %d" % (firstNumber, secondNumber , firstNumber + secondNumber))