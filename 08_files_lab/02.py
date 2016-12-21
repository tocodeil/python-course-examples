"""
ex02.py
merge 2 files into a third file

"""

import sys

line1 = " "
line2 = " "
(_, file1, file2, file3) = sys.argv


with open(file1,'r') as f1:
    with open(file2,'r') as f2:
        with open(file3,'w') as f3:
             while line1 != "" or line2 != "":
                line1 = f1.readline()
                line2 = f2.readline()
                f3.write(line1)
                f3.write(line2)


          

