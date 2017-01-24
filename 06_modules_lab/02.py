""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
"""

import sys

(x ,y) = sys.argv[1:]

x1= float(x)
x2= float(y)
print ("The sum of the two number is %f" % float(x1+x2))
