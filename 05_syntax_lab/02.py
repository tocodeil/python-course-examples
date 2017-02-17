"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""

import random
sum = 0

for number in range(7):
    x=random.randint(1,100)
    number += x 
    sum += number
    

print "sum = ",sum 

if sum % 7 == 0:
 print "boom"





  
  


 

 





