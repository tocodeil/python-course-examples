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

def iscomment(line):
    return re.search('^#', line)

def findValue(key, line):
    regexp = r'%s\s*=\s*(\w*)' % sys.argv[2]
    m = re.search(regexp, line)
    if m: return m.group(1)
    else: return None

with open(sys.argv[1], 'r') as fin:
    for line in fin:
        if not iscomment(line):
           value = findValue(sys.argv[2], line)
           if value != None:
               print value
               break


