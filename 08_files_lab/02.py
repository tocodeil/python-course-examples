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

filea = sys.argv[1]
fileb = sys.argv[2]

filec = 'c.txt'


with open(filea, 'r') as froma:
    with open(fileb, 'r') as fromb:
        with open(filec, 'w') as toc:
            newlist = list(itertools.izip_longest(froma, fromb, fillvalue=''))
            for item in newlist:
                for each in item:
                    toc.write(each)
