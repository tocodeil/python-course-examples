"""appent file to another"""
import os,sys
with open ('c:\python/week_2_2/file1.txt','w') as fout:
    for i in range(6,11):
        fout.write("I number ")
        fout.write(str(i))
        fout.write('\n')
with open ('c:\python/week_2_2/file2.txt','w') as fout:
    for i in range(1,6):
        fout.write("I number ")
        fout.write(str(i))
        fout.write('\n')
f1 = sys.argv[1]
f2 = sys.argv[2]
if not os.path.exists('c:\python/week_2_2/{0}'.format(f1)):
    print "there is no file with %s name" %f1
    quit()
if not os.path.exists('c:\python/week_2_2/{0}'.format(f2)):
   with open ('c:\python/week_2_2/{0}'.format(f2),'w') as fout:
    for i in range(1,6):
        fout.write("I number ")
        fout.write(str(i))
        fout.write('\n') 
with open ('c:\python/week_2_2/{0}'.format(f2),'a' ) as fapp:
    with open ('c:\python/week_2_2/{0}'.format(f1),'r'  ) as fin:
        for line in fin.read():
            fapp.write(line)
