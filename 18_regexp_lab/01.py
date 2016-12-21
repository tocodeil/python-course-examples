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

def get_value_by_key(text, key):
    m = re.search(r'^#', text)
    if m is not None:
        return None
    m = re.search(r'(\w+)\s*=\s*(\w+)', text)
    if m is not None:
        if m.group(1) == key:
            return m.group(2)
    return None

if len(sys.argv) != 3:
    print "Usage: %s <inifile> <key>" % sys.argv[0]
    sys.exit(1)

(_, inifile, key) = sys.argv

with open(inifile, "r") as fin1:
    for line in fin1:
        value = get_value_by_key(line, key)
        if value is not None:
            print value
