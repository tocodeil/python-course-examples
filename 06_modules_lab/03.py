""" Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.
- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested
- Take threshold and path as command line arguments
"""

import os
import argparse
import sys
searchfolder = str(sys.argv[1])
Minimumfilesize = int(sys.argv[2])
 

for root, dirs, files in os.walk(searchfolder):
 for file in files: 
 #  print file
   fp = os.path.join(root, file)
   currentfilesize = os.path.getsize(fp)
   if currentfilesize > Minimumfilesize:
       print "The file %s is bigger then 1MBy, to delete press Y or any key to conrinure " % fp,currentfilesize
       userinput= raw_input()
       if userinput == ('Y'):
        os.remove(fp)
       

      