"""
Write a program that takes 2 file names
and appends the second file's contents to
the end of the first one.

So if file 'a.txt' has:

a1
a2

and file 'b.txt' has

b1
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
    print "Usage: %s <fileToAppend> <fileToRead>" % sys.argv[0]
    sys.exit(1)

(_, fileToAppend,fileToRead) = sys.argv

bufsize = 20

with open(fileToAppend, "ab") as fout:
    with open(fileToRead, "rb") as fin:
        buf = fin.read(bufsize)
        while buf != "":
            fout.write(buf)
            buf = fin.read(bufsize)