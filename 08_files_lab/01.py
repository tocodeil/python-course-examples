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
#Path = sys.argv[1]
First_file = sys.argv[1]
Second_file = sys.argv[2]

with open(First_file, "r") as fin:
    with open(Second_file, "a") as fout:
        for line in fin:
            fout.write(line)




