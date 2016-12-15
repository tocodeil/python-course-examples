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
import os
import sys

if len(sys.argv) != 3:
    print "Usage: %s <filepath1> <filepath2>" % sys.argv[0]
    sys.exit(1)

(_, filepath1, filepath2) = sys.argv

if (os.path.exists(filepath1) and os.path.exists(filepath2)):
	with open(filepath1, "a") as file1:
		    with open(filepath2, "r") as file2:
				for line in file2:
					file1.write(line)


