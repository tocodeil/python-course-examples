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

folder_path = sys.argv[1]
size_data = sys.argv[2]

#working_directory = os.getcwd()
print("The current working directory is " + folder_path + "\nNow searching it for files larger than "+ size_data + " bytes")

for root, dirs, files in os.walk(folder_path):
    for size in files:
        path = os.path.join(root, size)
        file_size = os.stat(path).st_size

        if file_size >= int(size_data):
            print("The file " + path + "is larger than " + size_data + "\nDo you want to delete it? (yes/no)")
            answer = raw_input()
            if answer == "yes":
                print "deleting the file " + path
                os.remove(path)
            if answer == "no":
                print "OK, thank you"
        else:
            print("Did not meet criterion")
