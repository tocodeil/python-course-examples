#!/usr/bin/python
import re 
import sys, os

with open('csv', 'r') as f:
	for line in f:
		x = re.search(r',\b(\w+)', line)
		y = re.search(r'\b(\w+)' ,line)
		if x and y:
			line =  line.replace(y.group(1) , '!')
			line =  line.replace(x.group(1) , y.group(1))
			print line.replace( '!', x.group(1))