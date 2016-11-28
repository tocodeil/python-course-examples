"""
Write a program that generates a random number
between 1 and 10,000,
and prints the sum of its digits.
For example if the number was: 2345
the result should be: 14.
"""








from random import randint
sum=0
for x in range(0,7):
    random_number=randint(1,100)
    print(random_number)
    sum+=random_number
print "The sum is:" , sum
if sum%7==0:
    print "Boom"


    