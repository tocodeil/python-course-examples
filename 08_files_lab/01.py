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

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("outPath", type=str, help="display the first file path")
parser.add_argument("inPath", type=str, help="display the second file path")	
	
args = parser.parse_args()
outPath = args.outPath
inPath = args.inPath


with open(inPath,"r") as fin:
	with open(outPath, "a") as fout:
		for line in fin:
			fout.write(line)


