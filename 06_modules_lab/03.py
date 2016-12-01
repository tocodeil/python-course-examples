""" Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.

- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested

- Take threshold and path as command line arguments
"""



import os

print "Enter a path: "
path =raw_input()
for root, dirs, files in os.walk(path):
    for name in files:
        filename = os.path.join(root, name)
        if os.path.getsize(filename)/1024>=1024:
            print "The size of %s is above 1 MB, Would you like to delete this file (Y/N)? " % name
            if raw_input().lower() =="y":
                os.remove(filename)
            else:
                print "else" 
                continue