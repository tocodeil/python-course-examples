"""get name and password and check if it correct"""
import os,sys
nep = {'apple' : "red" , 'lettuce' : "green" , 'lemon' : "yellow" , 'orange' : "orange"}
for key in nep:
    if sys.argv[1] == key and nep[key] == sys.argv[2] :
        print "Welcome Master"
        quit()
print "INTRUDER ALERT"