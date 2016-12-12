"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""
c = []


letters = range(ord('a'),ord('z')+1)

c += [chr(a)+chr(b)+chr(c) for a in letters for b in letters for c in letters]
print c