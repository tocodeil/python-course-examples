""" Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.

- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested

- Take threshold and path as command line arguments
"""


import os
cwd = os.getcwd()

for file in os.listdir("."): 
      file_path = cwd+"\\"+file
      #print file_path
      statinfo = os.stat(file_path)
      #print statinfo.st_size

      size_of_file = int(statinfo.st_size)
      if (size_of_file > 1000):
           print "File name is :" , file
           print "please type 1 if you want to delete the file else type 0 :"
           chooice = int(raw_input())

           if (chooice == 1):
                 os.remove (file_path)

