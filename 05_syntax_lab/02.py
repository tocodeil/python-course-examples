"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""

total=0

from random import randint
for _ in range(7):
    i= randint(1, 100)
    print i
    total += i
print  total    
if total %7 ==0: 
    print "boom"
    

