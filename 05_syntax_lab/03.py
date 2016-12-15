"""
Write a program that generates a random number
between 1 and 10,000,
and prints the sum of its digits.
For example if the number was: 2345
the result should be: 14.
"""

from random import randint

randNum = randint(1,10000)

# print(randNum)

result = 0

for x in str(randNum):
	result += int(x)
	
print(result)