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
import itertools 
import sys 

(inPathOne, inPathTwo, outPath) = sys.argv[1:]


with open(inPathOne,"r") as finOne:
	with open(inPathTwo,"r") as finTwo:
		with open(outPath, "w") as fout:
			newlist = list(itertools.izip_longest(finOne, finTwo, fillvalue=''))
			for item in newlist:
				for node in item:
					fout.write(node)