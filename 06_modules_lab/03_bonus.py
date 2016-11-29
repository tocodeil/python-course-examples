import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--folderpath", help="folderpath to check",
                    type=str)

parser.add_argument("--sizeMB", help="minimum size to check",
                    type=int, choices=range(1, 101))


args = parser.parse_args()
src = args.folderpath
size = args.sizeMB*1024*1024

#print src
#print size

for root, dirs, files in os.walk(src, topdown=False):
    for name in files:
        #print(os.path.join(root, name))
        filename = os.path.join(root, name)
        size_in_mb = os.path.getsize(filename)
        if size_in_mb > size:
            print 'filename {path} with size {size} MB'.format(path=name, size=size_in_mb/(1024*1024))
            answer = raw_input('would you like to delete the file {name}? (y/n)')
            if answer == 'y':
                os.remove(filename)
                print 'file {0} removed'.format(filename)

