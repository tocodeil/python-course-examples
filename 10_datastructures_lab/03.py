#!/usr/bin/python

import sys

with open('/homes/dani/Desktop/hosts.txt', 'r') as file1:
    for compName in file1:
        y = str(compName.split("=")[1])
        j = compName.split("=")[0]
        for i in sys.argv[1:]:
            if i == j:
               print i
               break
            else:
                print "Not Found"
