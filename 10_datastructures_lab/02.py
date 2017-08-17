#!/usr/bin/python

import sys

avg =sum([int(i) for i in sys.argv[1:]]) / (len(sys.argv) -1 )

print "Average is: ", avg
print "Above average: ", [int(i) for i in sys.argv[1:] if int(i) > avg]
