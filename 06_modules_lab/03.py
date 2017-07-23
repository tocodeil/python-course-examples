"""remove big file"""
import os,sys
if len(sys.argv) < 2 :
    path = 'c:\python/week 2'
else:
    path = sys.argv[1]
for i in os.listdir(path):  
    x = int(os.stat(i).st_size)
    if x > 1024:
        print i
        if raw_input("do you want to remove this big file %s ?" %(i)) == "yes" :
            os.remove(i)