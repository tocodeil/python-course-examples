#!/usr/bin/python
import sys
print  str([l1 for l1 in sys.argv[1]  if l1 in sys.argv[2]]).strip('[]').replace("'" , "")