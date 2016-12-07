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

if len(sys.argv) != 3:
    print "Usage: %s <threshold> <path>" % sys.argv[0]
    sys.exit(1)

(_, threshold,path) = sys.argv

for root,dirs,files in os.walk(r"%s" % path):
	print(files)
	for file in files:
		filepath = os.path.join(root, file)
		if(os.path.getsize(filepath) > int(threshold)):
			print("File %s is bigger than threshold. Delete it? (Y/N)" % file)
			decision = raw_input()
			if(decision == "Y"):
				os.remove(filepath)

