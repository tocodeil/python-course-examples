#!/usr/bin/python
import sys, os 
print  str([int(x) for x in sys.argv[1:21] if int(x) > (sum(([int(grade) for grade in sys.argv[1:21]]))/20)]).strip('[]')
