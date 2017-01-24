""" Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.

- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested

- Take threshold and path as command line arguments
"""
import os
import sys
try:
	if len(sys.argv) != 3 :
		raise TypeError()
	else:
		threshold = sys.argv[1]
		path = sys.argv[2]
		for file in os.listdir("."):
			if os.stat(path+"\\"+file).st_size > long(threshold):
				print(file)
				print ("Do you want to delete this file? type (yes/no)")
				if raw_input().lower()== 'yes':
					os.remove(path+"\\"+file)
					print("The file %s was deleted!" % (file))
except  TypeError:
	print ("Usage: %s <threshold> <path>" % sys.argv[0])
	sys.exit(1)