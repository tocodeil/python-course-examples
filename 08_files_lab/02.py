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


x = sys.argv[0]
y = sys.argv[1]
Z = sys.argv[2]

with open (x, "r") as READ1 :
    for line1 in READ1:
        with open (y, "r") as READ2 :
            for line2 in READ2 :
                with open (Z, "a") as WRITE3 : 
                    WRITE3.write (line1)
                    WRITE3.write (line2)



