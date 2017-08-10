#!/usr/bin/python

import sys
from itertools import izip_longest

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]

with open(file1,"r") as infile1:
    with open(file2, "r") as infile2:
         with open(file3, "w") as outfile:
            for i, j in izip_longest(infile1, infile2):
                if i:
                    outfile.write(i)
                if j:
                    outfile.write(j)