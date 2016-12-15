""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
"""
import sys
if len(sys.argv) < 3:
   print "error"
   sys.exit(1)
num1=sys.argv[1]
num2=sys.argv[2]
try:
   val1 = int(num1)
   val2 = int(num2)
except ValueError:
   print "error"
   sys.exit(1)
num1=int(sys.argv[1])
num2=int(sys.argv[2])
print num1+num2
