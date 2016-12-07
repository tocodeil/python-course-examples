
from collections import Counter

word1 = raw_input("Enter a word")
word2 = raw_input("Enter a word again")


lst_word1 = Counter(word1)
lst_word2 = Counter(word2)

if len(lst_word1) >= len(lst_word2):
    first = lst_word1
    second = lst_word2
else:
    first = lst_word2
    second = lst_word1

for i in first:
    for j in second:
        if i == j:
            print i
