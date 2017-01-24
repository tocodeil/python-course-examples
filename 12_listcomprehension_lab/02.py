"""
Write a python program that takes two words
as sys.argv and prints only the letters
common to both
"""
import sys

word1 = sys.argv[1]
word2 = sys.argv[2]

common = [letter for letter in word1 for b in word2 if letter == b]
print common
