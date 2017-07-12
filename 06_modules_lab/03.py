#!/usr/bin/python
import sys
import os 
MB_IN_B= 1048576
file_to_delete = []
dir_location = sys.argv[1]
size_wanted = int(sys.argv[2])
print dir_location
print size_wanted

for root, subDirs , files in os.walk(dir_location):
		for subDir in subDirs:
			for f in files:
				if os.path.getsize(os.path.join(root,f)) > size_wanted*MB_IN_B: 
					file_to_delete.append(os.path.join(root,f))
if raw_input('would yo like delete all files that are bigger then %s mb  ' % size_wanted ) == 'yes':
	for file_name in file_to_delete:
		if os.path.exists(file_name):
			print 'removing: %s' % file_name
			os.remove(file_name) 
