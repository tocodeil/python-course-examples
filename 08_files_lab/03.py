""" add to numbers from csv file"""
import os,sys
import csv
sum = 0
with open ('c:\python/week_2_2/bool.csv','r') as csvin :
    reader = csv.reader(csvin)
    for row in reader:
        sum+= int(row[1])
print sum