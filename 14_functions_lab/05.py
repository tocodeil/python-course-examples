#!/usr/bin/python
from collections import defaultdict
def group_by(fun , *args):
	dic =defaultdict(list)
	for arg in args[1:]:
		dic[fun(arg)].append(arg)
	return dic	
