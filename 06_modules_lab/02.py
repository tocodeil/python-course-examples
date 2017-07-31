#!/usr/bin/python
import sys

if (len(sys.argv)!=3):
    print "wrong usage"

else:
    num1 = sys.argv [1]
    num2 = sys.argv [2]
    if not (str(num1).isdigit()):
        print "invalid"
    elif not (str(num2).isdigit()):
        print "invalid"
    else:
        print int(num1) + int(num2)