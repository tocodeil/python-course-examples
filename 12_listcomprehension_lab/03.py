"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""

letters =  [chr(x) for x in range(ord('a'), ord('z')+1)]

print [x+y+z for x in letters for y in letters for z in letters]