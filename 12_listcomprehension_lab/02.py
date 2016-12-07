"""
Write a python program that takes two words
as sys.argv and prints only the letters
common to both
"""
import sys

first_word = sys.argv[1]
second_word = sys.argv[2]

first = sorted(list(first_word))
second = sorted(list(second_word))
#print first
#print second

for letter in first:
    if letter in second:
        print letter