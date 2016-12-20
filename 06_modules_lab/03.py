"""
module_ex03.py

"""
import os
import sys

if len(sys.argv) != 3:
    print "wrong number of auguments, exiting..."
    sys.exit()

(_, file_size, folder_path) = sys.argv

for root, dirs, files in os.walk(folder_path):
    for name in files:
        print os.stat(root + "\/" + name).st_size/1024/1024
        if os.stat(root + "\/" + name).st_size/1024/1024 > float(file_size):
            print "file  %s size is:%s MB" % (name, os.stat(root + "\/" + name).st_size/1024/1024)
            print "do you wish to delete file ? (Y/N)"
            to_delete=raw_input()
            
            
            if to_delete.upper() == "Y":
                os.remove(root + "\/" + name)