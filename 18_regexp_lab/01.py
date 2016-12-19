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
(filename, key) = sys.argv[1:]
keys = {}
data=[]
with open(filename, "r") as fin1:
    for line in fin1:
        #print line
        match = re.search('^\w+\s*=\s*(\w+)',line)
        if match:
            data = match.group(0).split('=')
            data = [x.strip(' ') for x in data]  
            print data
            keys[data[0]]=data[1]
        
print keys.get(key)

