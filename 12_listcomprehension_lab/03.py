"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""

letters = ['a', 'b', 'c']
print [c1+c2+c3 for c1 in letters for c2 in letters for c3 in letters]