#!/usr/bin/python
import sys, os
from collections import Counter , defaultdict
s = set()
f = [word.strip('\n') for word in open(sys.argv[1])]
d =list()
for word in f:
	for w in f:
		if Counter(word) == Counter(w):
			d.append(w)
	s.add(str(d))		
	d = list()
for i in s:
	print i.strip('[]').replace("'","")