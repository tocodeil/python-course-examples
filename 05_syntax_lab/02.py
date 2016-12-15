"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""
from random import randint

sum = 0
for i in range(7):
    sum += randint(1,100)

print(sum)
if(sum % 7 == 0):
    print("Boom")