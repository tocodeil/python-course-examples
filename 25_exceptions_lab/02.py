"""
Write a program that takes a file name
and prints line count for the file

Alert the user politely if there was any problem opening the file
"""

import sys

filename = sys.argv[1]

try:
    with open(filename, 'r') as read:
        counter = 0
        for line in read:
            counter += 1
    print counter
except:
    print "Sorry, file %s not found" % filename