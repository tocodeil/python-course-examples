"""
Write a python program that takes numbers in a loop
and for each number prints its square root
If value is negative or not a number show 
a warning and keep reading values
"""

import math
import sys


while True:
    a = raw_input()
    if a == "": break  
    try:
        print math.sqrt(int(a))
    except Exception as e:
        print e.message
   

      


         
     
        