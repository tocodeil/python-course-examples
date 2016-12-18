"""
Write a python program that takes numbers in a loop
and for each number prints its square root
If value is negative or not a number show 
a warning and keep reading values
"""

import math

print "Please enter a number"
while True:
    x = raw_input(">")
    try:
        number = float(x)
        print math.sqrt(number)
    except ValueError as e:
        if e.message == "math domain error":
            print "Positive numbers only"
        else:
            print "You must enter numbers only"
