""" Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.

- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested

- Take threshold and path as command line arguments

Bonus: Use argparse module to parse command line arguments
"""

import os
import argparse
import sys
try:
	parser = argparse.ArgumentParser()
	parser.add_argument("threshold", type=long, help="display a threshold of a file size")
	parser.add_argument("path", type=str, help="display the current working directory path")	
	args = parser.parse_args()
	threshold = args.threshold
	path = args.path
	for file in os.listdir("."):
		if os.stat(path+"\\"+file).st_size > long(threshold):
			print(file)
			print ("Do you want to delete this file? type (yes/no)")
			if raw_input().lower()== 'yes':
				os.remove(path+"\\"+file)
				print("The file %s was deleted!" % (file))
except :
	sys.exit(1)