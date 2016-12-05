"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""
print "good day Yo"
import random

summ =0
for n in range (7):
   summ =summ + random.randint (0,100)  

print summ
if summ%7==0:
    print "Boom"
    
