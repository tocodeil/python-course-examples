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

# The requirements on this file are different from the one on the site.
# Following the requirements on this file.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename1", type=str, help="First filename.")
parser.add_argument("filename2", type=str, help="Second filename.")
args = parser.parse_args()

with open(args.filename2, "r") as fin:
    with open(args.filename1, "a") as fout:
        for line in fin:
            fout.write(line)
