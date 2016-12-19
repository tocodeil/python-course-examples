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
my_key = sys.argv[2:]
grouped = {}

with open(file_name, 'r') as property:
    for line in property:
        locate = re.search(r'(\w+)\s*=\s*(\w+)', line)

        if locate:
            keys = locate.group(1)
            values = locate.group(2)
            grouped[keys] = values

    #print grouped

for item in my_key:
    print grouped[item]
