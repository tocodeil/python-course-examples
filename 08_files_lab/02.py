"""
ex02.py
merge 2 files into a third file

"""

import sys

line1 = " "
line2 = " "
(_, file1, file2, file3) = sys.argv

f1 = open(file1,'r') 
f2 = open(file2,'r') 
f3 = open(file3,'w') 

line1 = f1.readline()
line2 = f2.readline()

while line1 != "" or line2 != "":
    f3.write(line1)
    f3.write(line2)
    line1 = f1.readline()
    line2 = f2.readline()


f1.close()
f2.close()
f3.close()            

