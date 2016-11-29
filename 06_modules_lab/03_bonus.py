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
import sys
import argparse

parser = argparse.ArgumentParser(description='Delete large files.')
parser.add_argument('root', nargs='?', default='.', help='the root folder')
parser.add_argument('size',  nargs='?', default=1000000, type=int, help='the minimal size of files to delete')
args = parser.parse_args()

for path, dirnames, filenames in os.walk(args.root):
  for name in filenames:
    fullPath = os.path.join(path,name)
    size = os.path.getsize(fullPath)
    if (size > args.size):
      if (raw_input("Delete file %s (size=%dB)? Y/N:" % (fullPath, size)).lower() == "y"):
        print "Deleting %s" % fullPath
        os.remove(fullPath)
     
  