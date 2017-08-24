#!/usr/bin/python

from itertools import combinations_with_replacement

a_to_z =[(chr(x)) for x in range(97, 123)]

comb_list = [y for y in combinations_with_replacement(a_to_z, 3)]

print comb_list
