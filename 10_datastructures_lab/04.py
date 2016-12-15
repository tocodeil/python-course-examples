"""
Write a program that finds anagrams in a words file
Program takes a path to a words file, 
reads the file and searches for words with the same letters.
All words with the same letters should be printed together
"""

words_file = raw_input("Insert words file path: ")

with open (words_file, 'r') as fout:
    anag_dict = {} 
   
    for word in fout:
        w = ''.join(sorted(word))
        anag_dict.setdefault(w, []).append(word[:-1])
    for anag_list in anag_dict.values():
        print ' '.join(anag_list)