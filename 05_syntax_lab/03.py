"""
Write a program that generates a random number
between 1 and 10,000,
and prints the sum of its digits.
For example if the number was: 2345
the result should be: 14.
"""

from random import randint

num = randint(1, 10000)
sum = 0

for i in range(6):
    sum += num % 10
    num = num / 10

print(sum)