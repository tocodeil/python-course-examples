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
with open ('input.csv', 'rb') as csvfile:
    readline = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for line in readline:
        match1 = re.search('\'[a-zA-Z]*',str(line))
        match2 = re.search('\,[a-zA-Z]*\,',str(line))
        match3= re.search('[a-zA-Z]*@[A-Za-z]*\.[A-Za-z]*',str(line))
        newformat.append(match2.group(0))
        newformat.append(match1.group(0))
        newformat.append(match3.group(0))
print newformat
        