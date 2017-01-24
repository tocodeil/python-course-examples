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
import itertools

if len(sys.argv) != 4:
    print "Usage: %s file1 file2 file3" % sys.argv[0]
    sys.exit(1)

with open(sys.argv[1], "r") as f1:
    with open(sys.argv[2], "r") as f2:
        with open (sys.argv[3], "w") as fout:
            for lines in itertools.izip_longest(f1, f2):
                for line in lines:
                    if line != None:
                        fout.write(line)



