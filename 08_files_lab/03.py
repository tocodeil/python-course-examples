#!/usr/bin/python
import sys
import csv

fileToOpen = sys.argv[1]

with open(fileToOpen, "r") as csvfile:
    total = 0
    csvFile = csv.reader(csvfile)
    for row in csvFile:
        i = row[1]
        total += int(i)
print total
