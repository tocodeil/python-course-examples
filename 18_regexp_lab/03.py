"""
Write a python program that takes a CSV file
reads it line by line and prints each line
with first and second columns reversed.
Sample input:
    Shana,Sargent,shanasargent@isoswitch.com
    Witt,Hampton,witthampton@zaphire.com
    Morgan,Grant,morgangrant@lotron.com
Sample output:
    Sargent,Shana,shanasargent@isoswitch.com
    Hampton,Witt,witthampton@zaphire.com
    Grant,Morgan,morgangrant@lotron.com
"""
import csv
import re
data = []
newformat = []
with open ('input.csv', 'r') as fin:
    for line in fin:
        match = re.split(',',line)
        print ("%s" % match[1],match[0],match[2])

