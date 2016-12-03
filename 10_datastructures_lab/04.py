"""
Write a program that finds anagrams in a words file
Program takes a path to a words file, 
reads the file and searches for words with the same letters.
All words with the same letters should be printed together
"""
import collections

wordDic = collections.defaultdict(list)

with open("words", "r") as fin:
    for line in fin:
        stripped = line.strip()
        if not stripped:
            continue

        sortedWord = sorted(stripped)
        key = "".join(sortedWord)
        wordDic[key].append(stripped)

for words in wordDic.values():
    print " ".join(words)
