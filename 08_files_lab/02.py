import itertools
import sys

First_file = sys.argv[1]
Second_file = sys.argv[2]
Sum_file = sys.argv[3]

with open(First_file, "r") as fin1:
    with open(Second_file, "r") as fin2:
        with open(Sum_file, "a") as fout:
             line = itertools.izip_longest(fin1, fin2, fillvalue='')
             for each in line:
                 for word in each:
                    fout.write(word)



