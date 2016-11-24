""" Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.

- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested

- Take threshold and path as command line arguments
"""

import os

for file in os.listdir("."):
    if os.stat(file)[6] > 1048576:
        print file
        ask = raw_input("Do you want to delete this file ? Y / N")
        if ask == 'Y' or ask == 'y':
            os.remove(file)
            print "File has been deleted"
        elif ask == 'N' or ask == 'n':
            print "OK, maybe next time"
