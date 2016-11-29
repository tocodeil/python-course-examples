""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
"""

import sys

if len(sys.argv) != 3:
    print "Usage: %s <number> <number>" % sys.argv[0]
    sys.exit(1)

print int(sys.argv[1]) + int(sys.argv[2])
