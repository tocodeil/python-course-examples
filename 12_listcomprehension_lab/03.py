"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""

for x in range(97,123):
    for y in range(97,123):
        for z in range(97,123):
            print chr(x), chr(y), chr(z)

