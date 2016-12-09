"""
Write a python program that takes two words
as sys.argv and prints only the letters
common to both
"""
import sys

if len(sys.argv) !=3:
    print "Usage: %s <word1> <word2>" % sys.argv[0]
    sys.exit(1)

(_, word1 ,word2) = sys.argv

common_letters = set([letter for letter in word1 if letter in word2])

print "Common letters:"
for letter in common_letters:
    print letter