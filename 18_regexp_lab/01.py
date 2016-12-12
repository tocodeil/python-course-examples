"""
Write a program that reads data
from property files.
Each line in the file can either be:
    An empty line
    A comment line (Start with #)
    A property line (of the form key = value)

Write a program that takes a property file name and key
as command line arguments and prints the requested value
"""
import re

print "Please Enter file and key:"
file = raw_input()
key = raw_input()

with open (file , 'r') as foo:
	l= foo.readlines()
	for line in l:
		if re.search((r'^' + key),line):
			print line.split('=')[1].lstrip()
			

