#!/usr/bin/python
"""makes 2 random numbers and gets the lowest number that they both divde in without plus"""
from random import randint
num = (randint(1,10) , randint(1,10))
print num[0] , num[1]
for i in range(1, (num[0] * num[1]) +1 ):
	if i % num[0] == 0 and i % num[1] == 0:
	 print i
	 break
		 
		
		
		
 
