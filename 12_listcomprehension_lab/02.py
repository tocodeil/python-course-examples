"""
Write a python program that takes two words
as sys.argv and prints only the letters
common to both
"""

import sys
import string

word1 = sys.argv[1]
word2 = sys.argv[2]

similiar = [digit for digit in word1 if string.find(word2,digit) != -1]
print similiar