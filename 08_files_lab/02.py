"""
The program takes 3 names. The first two
are existing file names and the last is a new file name/
The program should write the lines from the first two 
files interwinded into the output file.

"""

import sys
import itertools

file1 = sys.argv[1]
file2 = sys.argv[2]
file3new = sys.argv[3]

with open (file3new ,'w') as fin:
	with open (file1 ,'r') as fout:
		line1 = fout.readlines()
	with open (file2,'r') as foo:
		line2 = foo.readlines()
	result = itertools.izip_longest(line1,line2,fillvalue='')
	l = list(result)
	text = ''
	for pair in l:
		if pair[0].replace('\n','') != '':
			text += pair[0].replace('\n','') + '\n'
		if pair[1].replace('\n','') != '':
			text += pair[1].replace('\n','')
		#text += pair[0] + pair[1]
	fin.write(text)
	print text
	
	