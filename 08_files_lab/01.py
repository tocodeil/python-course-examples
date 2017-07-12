#!/usr/bin/python
import sys, os

if len(sys.argv) == 1:
	sys.exit('usage %s <text file1> <text file2(optinal)>' % sys.argv[0])

if len(sys.argv) == 2:
	with open(sys.argv[1]) as f1:
		Text1 = f1
		with open('newFile.txt', 'w') as f2:
			for line in Text1:
				f2.write(line)
	sys.exit()			
elif len(sys.argv) == 3:
	with open(sys.argv[1]) as f1:
		Text1 = f1
		with open(sys.argv[2], 'a') as f2:
			for line in Text1:
				f2.write(line)
elif len(sys.argv) == 4:
	with open(sys.argv[1]) as f1:
		with open(sys.argv[2]) as f2:
			with open(sys.argv[3], 'a') as f3:
				for line in f1:
					f3.write(line)
				for line in f2:
					f3.write(line)

