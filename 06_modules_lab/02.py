""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
"""
import sys

if len(sys.argv) != 3:
    print "Usage: %s <num1> <num2>" % sys.argv[0]
    sys.exit(1)

(_, num1, num2) = sys.argv

print "Sum = %d" % (int(num1)+int(num2))
