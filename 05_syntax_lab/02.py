"""
Write a Python program that generates 7 random integers
between 1 and 100, and prints their sum.
If the sum is divisible by 7, also print the word "Boom".
"""
sumnum = 0
for _ in range(7):
  from random import randint
  num = randint(1, 100)
  sumnum = sumnum + num
if sumnum % 7 == 0: 
  print "sum of numbers is %d Boom " % sumnum 
else:
  print "sum of numbers is %d" % sumnum 
