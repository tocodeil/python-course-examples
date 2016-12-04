"""
Write a python program that takes two words
as sys.argv and prints only the letters
common to both
"""
import sys

first_word = set(sys.argv[1])
second_word = set(sys.argv[2])

print "Letters that found in both words : "
for letter in first_word & second_word:
    print letter
