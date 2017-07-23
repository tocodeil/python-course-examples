"""intsert 2 file to one, line by line"""
import os,sys
from itertools import izip_longest
f1 = sys.argv[1]
f2 = sys.argv[2]
f3 = sys.argv[3]
with open ('c:\python/week_2_2/{0}'.format(f1),'r') as fin1,open ('c:\python/week_2_2/{0}'.format(f2),'r') as fin2,open ('c:\python/week_2_2/{0}'.format(f3),'w') as fout :
    for line1,line2 in izip_longest(fin1,fin2):
        fout.write(line1)
        fout.write(line2)