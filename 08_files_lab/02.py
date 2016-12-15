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
from itertools import izip_longest
import sys
src1 = sys.argv[1]
src2 = sys.argv[2]
new = sys.argv[3]



with open(src1) as textfile1, open(src2) as textfile2:
    with open(new, "w") as out:
        for x, y in izip_longest(textfile1, textfile2,fillvalue=''):
         out.write("{0}{1}".format(x, y))
