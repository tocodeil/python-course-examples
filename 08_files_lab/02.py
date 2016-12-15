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

import os
import sys

if len(sys.argv) != 4:
    print "Usage: %s <filepath1> <filepath2> <outfilepath>" % sys.argv[0]
    sys.exit(1)

(_, filepath1, filepath2, outfilepath) = sys.argv

if (os.path.exists(filepath1) and os.path.exists(filepath2)):
	with open(outfilepath,"w") as out:
		with open(filepath1, "r") as file1:
		    with open(filepath2, "r") as file2:
				lines1 = file1.readlines()
				lines2 = file2.readlines()
				counter = 0
				for x in range(len(lines1)):
					out.write(lines1[x])
					if(x<len(lines2)):
						out.write(lines2[x])
					counter += 1	
				if(len(lines1) < len(lines2)):
						while(counter<len(lines2)):
							out.write(lines2[counter])
							counter += 1