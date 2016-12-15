"""
Write a program that finds anagrams in a words file
Program takes a path to a words file, 
reads the file and searches for words with the same letters.
All words with the same letters should be printed together
"""
words = []

with open('words') as wordsFile:
    for word in wordsFile:
        words.append(word.strip('\n'))


for word in words:
    for another_word in words:
        if set(otherWord) == set(otherWord) and word != anotherotherWord_word:
                print word , otherWord
                words.remove(word),words.remove(otherWord)

for other in words:
    print other