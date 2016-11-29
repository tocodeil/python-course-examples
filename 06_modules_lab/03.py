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

if (len(sys.argv) > 1):
  root = sys.argv[1]
else:
  root = '.'

try:
  if len(sys.argv) > 2:
    maxSize = int(sys.argv[2])
  else:
    maxSize = 1000*1000
except ValueError:
  print "usage: %s <folder> <max size>" % sys.argv[0]
  sys.exit()

print "checking folder", root

for path, dirnames, filenames in os.walk(root):
  for name in filenames:
    fullPath = os.path.join(path,name)
    size = os.path.getsize(fullPath)
    if size > maxSize:
      if raw_input("Delete file %s (size=%dB)? Y/N:" % (fullPath, size)) == "Y":
        print "Deleting %s" % fullPath
        os.remove(fullPath)
     
  