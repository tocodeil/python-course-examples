"""
The program generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, the program print the word "Boom".
"""
sum=0
import random

for num in range(7):
  num=random.randrange(1,100)
  sum=sum+num

print sum
if sum % 7 == 0:
	print 'Boom'
	
	