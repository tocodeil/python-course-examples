"""
The program generates 2 random numbers
and calculates their least common multiple,
that is the smallest number that is divisible
by both.

"""
import random

num1=random.randint(1,10)
num2=random.randint(1,10)
if num1>=num2:
  Multi=num1
else:
  Multi=num2
print num1,num2           #I added these line to check my code
while True:
  if Multi%num1 == 0 and Multi % num2 == 0:
    print Multi
    break
  else:
    Multi+=1