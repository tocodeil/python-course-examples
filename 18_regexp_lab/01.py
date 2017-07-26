#!/usr/bin/python
import re 
import sys, os
def print_value_from_key(config , key ):
	with open(config, 'r') as f:
		for line in f:
			keyValuePair = re.search(r'(\w+)\s*=\s*(\w+)', line)
			if keyValuePair:
				if re.match(keyValuePair.group(1) , key):
					print keyValuePair.group(2)

print_value_from_key(sys.argv[1] , sys.argv[2] )