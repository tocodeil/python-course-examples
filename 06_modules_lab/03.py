""" Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.

- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested

- Take threshold and path as command line arguments
"""

import sys
import os

if len(sys.argv) != 3:
    print "Usage: %s <dirpath> <threshold>" % sys.argv[0]
    sys.exit(1)

(_, dirpath,threshold) = sys.argv


for root,dirs,files in os.walk(dirpath):
    for name in files:
      fullname = "%s\\%s" % (root,name)
      filesize = os.stat(fullname).st_size
      if float(filesize) > float(threshold):
        print "%s size is %d. " % (fullname,filesize),
        print r"Do you want to delete it (y\n)?",
        answer = raw_input()
        if answer == 'y':
          os.remove(fullname)
        elif answer == 'Y':
          os.remove(fullname)
