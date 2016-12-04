"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""

for a in range(97,123):
    for b in range(97, 123):
        for c in range(97, 123):
            print (chr(a)+chr(b)+chr(c))