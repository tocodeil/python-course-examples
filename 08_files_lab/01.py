"""
The program takes 2 file names
and appends the second file's contents to
the end of the first one.

"""

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
with open(file2,"r") as fin:
	with open (file1,"a") as fout:
		fout.write('\n')
		for line in fin:
			fout.write(line)



