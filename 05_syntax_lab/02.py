"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""
#from random import randint
import random

sumOfNums = 0
for _ in range(7):
	sumOfNums += random.randint(1,100)
print ("The sum is: %d" % (sumOfNums))
if (sumOfNums % 7) == 0:
	print("Boom")