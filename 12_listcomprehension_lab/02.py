"""
Write a python program that takes two words
as sys.argv and prints only the letters
common to both
"""
import sys

words = sys.argv[1:] 

print list(set( [ c for c in words[0]  if c in words[1] ]))

