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


def value_from_key(line, key_name):
    if re.search("^" + key_name, line) is not None:
        return True
    else : return False
            

file = sys.argv[1]
key = sys.argv[2]

with open(file, "r") as fout:
        for line in fout:
            if value_from_key(line, key):
                sys.stdout.write(re.split("=[ ]*", line)[1])