"""
Write a program that finds anagrams in a words file
Program takes a path to a words file, 
reads the file and searches for words with the same letters.
All words with the same letters should be printed together
"""
"""
dicn = {}
with open(r'.\words') as words:
    for word in words:
        dicn[word.strip('\n')] = set(word.strip('\n'))

"""

word_list = []

with open(r'.\words') as words:
    for word in words:
        word_list.append(word.strip('\n'))


for word in word_list:
    for another_word in word_list:
        if set(word) == set(another_word) and word != another_word:
                print word , another_word
                word_list.remove(word),word_list.remove(another_word)

for rest in word_list:
    print rest






