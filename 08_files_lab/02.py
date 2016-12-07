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

"""(src1, src2,dst) = sys.argv[2:]"""

src1 = "C:\\Users\\cchaimov\\Documents\\Ex3_python\\1.txt"
src2 = "C:\\Users\\cchaimov\\Documents\\Ex3_python\\2.txt"
dst  = "C:\\Users\\cchaimov\\Documents\\Ex3_python\\3.txt"
                
with open(src1, "r") as fout1, open(src2, "r") as fout2:
        with open(dst, "w") as fin:
            lines = itertools.izip_longest(fout1,fout2,fillvalue = "")
            for i in lines:
                fin.write(str(i[0]))
                fin.write(str(i[1]))
            
