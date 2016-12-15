"""
Write a program that generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""

x = 0

import random
num = random.randint(1,1000000000000)

while x == 0:
	
	if (num % 7 == 0 and num % 13 == 0 and num % 15 == 0):
		print num
		x = 1
		
	else :
		num = random.randint(0,1000000000000)
	
	

