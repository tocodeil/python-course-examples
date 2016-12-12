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

import sys
import re

file_name = sys.argv[1]
par_name = sys.argv[2]


with open(file_name, 'r') as file_name:
    for line in file_name:''
        m = re.search(r'(.*\S)\s*\=\s*(\w+)',line)
        if m is not None and m.group(1) == par_name:
            print "The value of %s is %s" % (par_name ,m.group(2))
