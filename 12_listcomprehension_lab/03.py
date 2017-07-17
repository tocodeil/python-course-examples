#!/usr/bin/python
s = set()
all_small_letters = [chr(small) for small in range(97,123)]
for l in all_small_letters:
	for l2 in all_small_letters:
		for l3 in all_small_letters:
			s.add('%s%s%s' %(l,l2,l3))
for i in s:
	print i