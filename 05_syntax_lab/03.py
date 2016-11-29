"""
Write a program that generates a random number
between 1 and 10,000,
and prints the sum of its digits.
For example if the number was: 2345
the result should be: 14.
"""

from random import randint

number_count = []
random_number = str(randint(1, 10000))
print("The random number is " + random_number)

for num in random_number:
    number_count.append(int(num))

total_digits = 0
for digit in number_count:
    total_digits += digit

print("The sum of the number's digits is " + str(total_digits))

