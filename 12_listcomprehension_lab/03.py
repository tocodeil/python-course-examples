"""
Find and print all possible sequences
of 3 lowercase characters: aaa, aab, aac, ..., zzz
"""

import string

chr_lst = list(string.ascii_lowercase)

print list(set( [ c1+c2+c3 for c1 in chr_lst for c2 in chr_lst for c3 in chr_lst ]))

