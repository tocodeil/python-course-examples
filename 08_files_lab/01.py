"""
ex0.py
append file

"""

import sys


(_, file1, file2) = sys.argv

with open(file2,'r') as f2:
    with open(file1,'a') as f1:
        for line in f2:
            f1.write(line)
            