"""
Write a program that generates a random number
between 1 and 10,000,
and prints the sum of its digits.
For example if the number was: 2345
the result should be: 14.
"""
total=0
#sum=0
from random import randint
for i in range(1, 2):

     numbers = randint(1,1000)
     print " the random number is:", numbers
     orech= len(str(numbers))
for y in range (len(str(numbers))):
      sum = numbers % 10
      total+=sum
      numbers /= 10

print "the sum of the digits is:", total
