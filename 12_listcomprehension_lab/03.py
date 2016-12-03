"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""

import sys

seq = [(chr(a)+chr(b)+chr(c))
       for a in range(ord('a'), ord('z')+1)
       for b in range(ord('a'), ord('z')+1)
       for c in range(ord('a'), ord('z')+1)]

print seq
