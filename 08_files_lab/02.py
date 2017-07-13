#!/usr/bin/python
import sys , os
from itertools import izip_longest

with open(sys.argv[1]) as f1:
	with open(sys.argv[2]) as f2:
		with open(sys.argv[3], 'w') as f3:
			for line,line2 in izip_longest(f1,f2):
				if line:
					f3.write(line)
					print line
				if line2:
					f3.write(line2)

		
		

				

