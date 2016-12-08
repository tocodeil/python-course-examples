"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""

l = range(97,123)
digits = [chr(x) for x in l]
rez = [x + y + z for x in digits for y in digits for z in digits]
print rez