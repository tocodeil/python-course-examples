"""
The program generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""

import random

while True:
  num = random.randrange(1000000)
  if num % 7 == 0 and num % 13 == 0 and num % 15 == 0:
    break
print "The number is:" ,num   
