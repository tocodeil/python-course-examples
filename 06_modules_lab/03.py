""" The program searches current working directory
for files larger than 1MB. Every time you find such a file the program print
its name to the user.

"""

import os
import sys

path = sys.argv[1]
MinSize = int(sys.argv[2])
for root,dirs,files in os.walk(path):
	for name in files:
		full_path = root + '\\' + name
		statinfo = os.stat(full_path)
		if statinfo.st_size >= MinSize:
			print name, '\n' , "Do you want to delete the file? Enter yes or no"
			UserAnswer = raw_input()
			if (UserAnswer).lower() == 'yes':
				os.remove(full_path)
				print "Your file deleted successfully"
			elif (UserAnswer).lower() == 'no':
				pass
			
