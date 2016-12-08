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
import os
from itertools import izip_longest
from itertools import chain

(srcfile1, srcfile2, interfile) = sys.argv[1:]
interlist=[]
line1= []
line2 =[]
i=0 
with open(srcfile1, "r") as fin1:
 with open(srcfile2, "r") as fin2:

     for line in fin1:
      line1.append(line)
      
     for line in fin2:
      line2.append(line)
      
     interlist=list(izip_longest(line1,line2))
     interlist1=list(chain.from_iterable(interlist))
     for i in interlist1:
        if i ==None:
         interlist1.remove(i) 
print interlist1
with open(interfile, "w") as fout:
   for line in interlist1:
    fout.write(str(line))