"""
Write a program that generates 2 random numbers
and calculates their least common multiple,
that is the smallest number that is divisible
by both.
For example if the numbers were 4 and 6,
program should print 12.
"""

from random import randint

first_number = randint(1, 10)
print("The first random number is " + str(first_number))
second_number = randint(1, 10)
print("The second random number is " + str(second_number))
common = first_number * second_number

if common % 2 == 0:
    print("The LCM is " + str(common /2))
else:
    for number in range (0, common):
        if number % first_number == 0 and number % second_number == 0:
            print("The LCM is " + str(number))
        else:
            continue