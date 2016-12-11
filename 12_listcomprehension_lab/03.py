"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""
c = []
 

letters = ['a','b','c']
c += [a+b+c for a in letters for b in letters for c in letters]
print c