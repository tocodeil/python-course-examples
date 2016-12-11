import sys
import os
import argparse

parser = argparse.ArgumentParser(description="Program to delete files larger than X size in defined folder")
parser.add_argument('-p','--path', help='Path of the Folder', required=True)
parser.add_argument('-s','--size', help='Size (MB) of files to delete', required=True)
args = vars(parser.parse_args())

path = args['path']
for root, dirs, files in os.walk(path):
    for name in files:
        filepath = os.path.join(root, name)
        if os.path.getsize(filepath)> 1000000 * float(args['size']):
             userInput = raw_input("{filename} -- Is bigger than {definedSize}MB, Do you wan to delete the file (Y/N)".format(filename = filepath, definedSize = float(args['size'])))
             if userInput == "Y":
                 os.remove(filepath)