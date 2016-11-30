"""
The program generates a random number
between 1 and 10,000,
The program prints the sum of its digits.
"""


sum=0
import random
num=random.randrange(10000)
print num                   #I added this line to check

while num != 0:
  digit=num%10
  num=num/10
  sum=sum+digit

print sum                  
