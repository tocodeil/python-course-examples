import sys
import os
path = sys.argv[1]
for root, dirs, files in os.walk(path):
    for name in files:
        filepath = os.path.join(root, name)
        if os.path.getsize(filepath)> 1000000 * float(sys.argv[2]):
             userInput = raw_input("{filename} -- Is bigger than {definedSize}MB, Do you wan to delete the file (Y/N)".format(filename = filepath, definedSize = float(sys.argv[2])))
             if userInput == "Y":
                 os.remove(filepath)