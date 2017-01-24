"""
Write a program that finds anagrams in a words file
Program takes a path to a words file, 
reads the file and searches for words with the same letters.
All words with the same letters should be printed together
"""

import sys

if len(sys.argv) != 2:
    print "usage: %s filename" % sys.argv[0]
    sys.exit(-1)

anagrams = {}

with open(sys.argv[1], "r") as fin:
    for line in fin:
        for word in line.split():
            key = ''.join(sorted(word))            
            if key in anagrams:
                anagrams[key] = "%s %s" % (anagrams[key],word)
            else:
                anagrams[key] = word

for key in anagrams:
    print anagrams[key]
