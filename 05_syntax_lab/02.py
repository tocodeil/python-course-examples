"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""

# Rand 7 numbers and print its sum : 
n = 1
sum = 0

import random
while n <= 7:
    rand_num = random.randint(0, 100)
    sum = sum + rand_num
    n = n + 1

    # check if the random number is equal to seven : 
    if rand_num == 7:
        print "boom" 

# print the sum of all numbers : 
print "sum is :", sum

