"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""

from random import randint

sum = 0

for number in range(7):
    randNum = randint(1, 100)
    print("The following number was randomally generated: %d") %randNum
    sum += randNum
    if randNum % 7 == 0:
        print "Boom!"
    else:
        continue

print("The sum of these numbers is = %d") %sum