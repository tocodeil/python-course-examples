""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
"""

import sys

if len(sys.argv) != 3:
    print "Usage: %s <num1> <num2>" % sys.argv[0]
    sys.exit(1)

sum = float(sys.argv[1]) + float(sys.argv[2])
print "%s + %s = %.3f" % (sys.argv[1], sys.argv[2], sum)