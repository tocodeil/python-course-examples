"""
Write a program that takes 3 names. The first two
are existing file names and the last is a new file name/
The program should write the lines from the first two 
files interwinded into the output file. So if we have

a.txt with
a1
a2

and b.txt with
b1
b2

then running

python 02.py a.txt b.txt c.txt
will result in the creation of c.txt with the following content:

a1
b1
a2
b2

"""

import sys
from itertools import izip_longest

(src1, src2, dst) = sys.argv[1:]

with open(src1, "r") as source1, open(src2, "r") as source2:
    with open(dst, "w") as destination:
        for line_a, line_b in izip_longest(source1, source2, fillvalue = ''):
            destination.write(str(line_a))
            destination.write(str(line_b))