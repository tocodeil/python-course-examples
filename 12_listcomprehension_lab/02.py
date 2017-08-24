#!/usr/bin/python

import sys

word1 = sys.argv[1]
word2 = sys.argv[2]

list_check = str([x for x in word1 if x in word2])
print list_check