"""
Write a python program that takes numbers in a loop
and for each number prints its square root
If value is negative or not a number show 
a warning and keep reading values
"""

import sys
import math

while True:
    num = raw_input()
    if num == "":
        break
    try:
        number = float(num)
        sqrt = math.sqrt(number)

    except ValueError as e:
        print "Please use positive numbers only. The error was: %s" % e.message

    else:
        print "The sqrt of %f is %f" % (number, sqrt)