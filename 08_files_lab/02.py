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
import sys
import itertools

if len(sys.argv) != 4:
    print "Usage: %s <infile1> <infile2> <outfile>" % sys.argv[0]
    sys.exit(1)

(_, infile1,infile2,outfile) = sys.argv

bufsize = 20
lines1 = []
lines2 = []
with open(outfile, "w") as fout:
    with open(infile1, "r") as fin1:
        lines1 = [line.rstrip('\n') for line in fin1]
    with open(infile2, "r") as fin2:
        lines2 = [line.rstrip('\n') for line in fin2]
    combinedLines = list(itertools.izip_longest(lines1, lines2, fillvalue=''))
    for line in combinedLines:
        if len(line[0]) > 0:
            fout.write(line[0] + '\n')
        if len(line[1]) > 0:
            fout.write(line[1] + '\n')
