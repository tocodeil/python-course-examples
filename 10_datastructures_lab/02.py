""" get 20 grades from user and print only the big from the average"""
import os,sys
sumi = 0 
for i in sys.argv[1:] :
    sumi += int(i)
avg = float(sumi) / len(sys.argv[1:])
for i in sys.argv[1:] : 
    if int(i) > avg :
        print i,