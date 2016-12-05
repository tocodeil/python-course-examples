"""
Write a python program that takes two words
as sys.argv and prints only the letters
common to both
"""
import sys

letters1 = set(sys.argv[1])
letters2 = set(sys.argv[2])

print [x for x in letters1 if x in letters2]

