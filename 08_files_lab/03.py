#!/usr/bin/python
import csv
import sys
sum_of_row2 = 0
f = open(sys.argv[1], 'rt')
reader = csv.reader(f)
for row in reader:
    sum_of_row2 += int(row[1])
f.close()
print sum_of_row2