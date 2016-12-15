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
import sys

file_name = sys.argv[1]

with open(file_name + ".csv" , 'rb') as excel:
    reader = csv.reader(excel)
    for row in reader:
        print row[1] + ",", row[0] + ",", row[2]