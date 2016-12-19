""" 
Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.

- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested

- Take threshold and path as command line arguments
"""

import os
import sys

(_, path, sizeInMB) = sys.argv

for name in os.listdir(path):
    if os.path.getsize(name) / 1024 > int(sizeInMB):
        print "Found file: %s bigger than 1MB. Delete? y/n" % name
        result = raw_input()
        if result.lower() == "y":
            os.remove(name)
            print "%s deleted." % name
