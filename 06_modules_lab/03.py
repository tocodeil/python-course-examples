#!/usr/bin/python
import sys
import os

location = sys.argv[1]
size_in_mb = int(sys.argv[2])
b_to_mb = 1048576
filesToDel = []

for root, dirs, files in os.walk(location):
    for directory in dirs:
        for i in files:
            x = os.path.join(root,i)
            if os.path.isfile(x) and os.path.getsize(x) <= size_in_mb * b_to_mb:
                filesToDel.append(x)
                print x
if raw_input('delete?') == 'y':
    for y in filesToDel:
        print y
        os.remove(y)