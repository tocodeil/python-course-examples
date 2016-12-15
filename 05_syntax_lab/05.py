"""
Write a program that generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""
while True:
 from random import randint
 num = randint(1, 1000000)
 if num % 7 == 0 and num % 13 == 0 and num % 15 == 0: 
  print "The number %d is divisable by 7,13 and 15" % num 
  break
