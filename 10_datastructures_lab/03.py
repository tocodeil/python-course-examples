"""
A file named hosts holds hostnames and IP addresses
in format: hostname=ip
Write a program that reads the file and takes
a list of hostnames in sys.argv
Program should print the IP addresses of the hosts requested
"""

import sys

args = sys.argv
test = {}
with open("hosts") as hostsParsed:
    for line in hostsParsed:
        (key, val) = line.strip().split('=')
        test[key] = val
for i in args:
    for j in test:
        if i == j:
            print i,test[i]




















