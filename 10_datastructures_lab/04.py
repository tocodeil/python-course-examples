"""
Write a program that finds anagrams in a words file
Program takes a path to a words file, 
reads the file and searches for words with the same letters.
All words with the same letters should be printed together
"""
import sys

#Get input
hosts_count = len(sys.argv) - 1

if len(sys.argv) < 2:
    print "Usage: %s <filepath>" % sys.argv[0]
    sys.exit(1)

(_, filepath) = sys.argv

#build dictionary
anagrams = {}
with open(filepath, "r") as fanagrams:
    for word in fanagrams:
        key = ''.join(sorted(word))
        val = anagrams.setdefault(key, "")
        anagrams[key] = val + " " + word.strip("\n")

#print output
for key in anagrams:
    print anagrams[key]
