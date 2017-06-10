"""
ex4.py
DB

"""
from collections import Counter


word_Dic = {}
letters = []
key=""

with open('words','r') as f:
    word_List = f.read().split()

for word in word_List:
    for letter in word:
        letters.append(letter)
    for s in sorted(letters):
        key = key + s
        
    if not key in word_Dic:
        word_Dic[key] =  word
    else:
        word_Dic[key] = word_Dic[key] + " " +  word
    key = ""
    letters = []
    
for i in  word_Dic:
    print word_Dic[i]

