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
import sys

fileName = sys.argv[1]
key =  sys.argv[2]


with open (fileName, 'r') as f:
	for line in f:
		search = re.search(r'(.*\S)\s*\=\s*(\w+)',line)
        if search is not None and search.group(1) == key:
            print "The value of key: %s is: %s" % (key ,search.group(2))