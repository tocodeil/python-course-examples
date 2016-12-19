"""
Write a program that takes 3 names. The first two
are existing file names and the last is a new file name/
The program should write the lines from the first two 
files interwinded into the output file. So if we have

a.txt with
a1
a2

and b.txt with
b1
b2

then running

python 02.py a.txt b.txt c.txt
will result in the creation of c.txt with the following content:

a1
b1
a2
b2

"""

import argparse
import os
import sys
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("source1", type=str, help="First filename.")
parser.add_argument("source2", type=str, help="Second filename.")
parser.add_argument("destination", type=str, help="Destination filename.")
args = parser.parse_args()

if os.path.isfile(args.destination):
    print "Destination file already exist."
    sys.exit(1)

if not os.path.isfile(args.source1):
    print "Source1 file do not exist."
    sys.exit(1)

if not os.path.isfile(args.source2):
    print "Source2 file do not exist."
    sys.exit(1)

with open(args.source1, "r") as fin1:
    with open(args.source2, "r") as fin2:
        with open(args.destination, "w") as fout:
            for key, val in itertools.izip_longest(fin1, fin2, fillvalue=""):
                fout.write(key)
                fout.write(val)


