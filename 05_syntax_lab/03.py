"""
Write a program that generates a random number
between 1 and 10,000,
and prints the sum of its digits.
For example if the number was: 2345
the result should be: 14.
"""

# Rand one number 

import random
num = random.randint(0, 10000)

# convert to string : 
num_string = str(num)

sum = 0
for y in num_string:
    y = int(y)
    sum = sum + y

print num_string
print sum

