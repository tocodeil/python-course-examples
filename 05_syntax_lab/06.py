"""
Write a program that generates 2 random numbers
and calculates their least common multiple,
that is the smallest number that is divisible
by both.
For example if the numbers were 4 and 6,
program should print 12.
"""

import random


num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

print num1
print num2

for i in range(1, num1 * num2 + 1):
    if i % num1 == 0 and i % num2 == 0:
        print i
        break


