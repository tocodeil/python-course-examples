""" Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.

- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested

- Take threshold and path as command line arguments
"""
import stat
import os
import sys
# print "Please insert your path"
Path = sys.argv[1]
file_size_for_delete = int(sys.argv[2])
file_size_for_delete = file_size_for_delete/1024/1024
for root, dirs, files in os.walk(Path):
    for name in files:
        file_size = os.stat(root + "\\" + name).st_size/1024/1024
        if file_size > file_size_for_delete:
            print "File %s/%s is Large than 1M and his size is: %sMB" % (root,name,file_size)
            print "Do you want to delete this file %s/%s? Yes/No" % (root,name)
            if str(raw_input()) == 'Yes':
                os.remove(root + "\\" + name)
                print "Your file deleted!"

