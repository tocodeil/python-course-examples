""" get ywo nuber and print their sum + check"""
import os,sys
if len(sys.argv) != 3 :
    print "we need exactlly 2 numbers"
    quit()
try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
except ValueError:
    print "please insert only numbers"
    quit()
print "the result is:", x + y
