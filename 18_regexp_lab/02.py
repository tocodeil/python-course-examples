#!/usr/bin/python
import re 
import sys, os
text = 'no_more_shall_we_part'
def under_scope_to_camelCase(text):
	x = re.sub(r'\_[a-z]' ,lambda m: m.group(0).upper()  , text)
	x = re.sub(r'_' , '' , x)
	print x

under_scope_to_camelCase(text)