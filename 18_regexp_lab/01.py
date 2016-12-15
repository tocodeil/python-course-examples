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

if len(sys.argv) != 3:
    print "usage %s <filename> <key>" % sys.argv[0]
    sys.exit()

comment_regex = re.compile('^#')
key_value_regex = re.compile(r'([^= ]*)\s*=\s*(.*)')

with open(sys.argv[1], 'r') as fin:
    for line in fin:
        if not comment_regex.search(line):
           match = key_value_regex.search(line)
           if match and match.group(1) == sys.argv[2]:
               print match.group(2)


