#!/usr/bin/python

import sys
import os

file1 = sys.argv[1]
file2 = sys.argv[2]


##bonus 1
if (len(sys.argv[1])!=3):
    print "no file input, this is a friendly error notice"

##bonus 2
if os.path.isfile(sys.argv[2]):
    file2type = "a"
else:
    file2type = "w"

with open (file1 , "r") as finput:
    with open (file2 , file2type) as foutput:
        for line in finput:
            foutput.write(line)