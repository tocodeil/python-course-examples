"""
Write a program that finds anagrams in a words file
Program takes a path to a words file, 
reads the file and searches for words with the same letters.
All words with the same letters should be printed together
"""

from collections import defaultdict

anagrams = defaultdict(set)

with open('words', 'r') as dictionary:
   for word in dictionary:
      word = word.rstrip()
      anagrams[''.join(sorted(word))].add(word)

#print anagrams

for key, value in anagrams.items():
    #print key
    for pair in value:
        #print pair
        print key, "-->", pair

#print anagrams.items()
