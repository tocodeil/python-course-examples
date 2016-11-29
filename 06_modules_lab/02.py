""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
"""

import sys

try:
    num1=float(sys.argv[1])
    num2=float(sys.argv[2])
    print (num1+num2)
except:
    print"Wrong parameters, Please insert two numbers"


