"""
Write a program that generates a random number
between 1 and 10,000,
and prints the sum of its digits.
For example if the number was: 2345
the result should be: 14.
"""
import random
number = (random.randint(1, 10000))
sum = 0
print number
for i in range (5):
    modul = number % 10
    sum = sum + modul
    number = number / 10

print sum


