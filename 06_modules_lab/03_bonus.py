#!/usr/bin/python
import sys
import os 
import argparse
parser = argparse.ArgumentParser(description = "Copy a json's lut file from SL to the review dir.")
parser.add_argument('-s', '--size_wanted', type=int, default = 1)
parser.add_argument('-d', "--dir", type=str, required=True )
args = parser.parse_args()
MB_IN_B= 1048576
file_to_delete = []
for root, subDirs , files in os.walk(args.dir):
		for subDir in subDirs:
			for f in files:
				if os.path.getsize(os.path.join(root,f)) > args.size_wanted*MB_IN_B: 
					file_to_delete.append(os.path.join(root,f))
if raw_input('would yo like delete all file that are bigger then %s mb  ' % args.size_wanted ) == 'yes':
	for file_name in file_to_delete:
		if os.path.exists(file_name):
			print 'removing: %s' % file_name
			os.remove(file_name) 
