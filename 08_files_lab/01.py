"""
Write a program that takes 2 file names
and appends the second file's contents to
the end of the first one.

So if file 'a.txt' has:

a1
a2

and file 'b.txt' has

b2
b2
b3

then after running
   python 01.py a.txt b.txt
a.txt will have

a1
a2
b1
b2
b3

and b.txt will have

b1
b2
b3

"""

import sys

if len(sys.argv) != 3:
    print "Usage: %s file1 file2" % sys.argv[0]
    sys.exit(1)

with open(sys.argv[1], "a") as fout:
    with open(sys.argv[2], "r") as fin:
        for line in fin:
            fout.write(line)


