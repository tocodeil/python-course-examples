
"""
This code is random in loop numbers in range 1-1000000 until finding a number that can be whole divide of 7,13 and 15
"""

from random import randint
number = randint(1, 1000000)
Flag = True
common_denominator = 1365 # 1365 is the multiplication of 7,13 and 15
while Flag:
  if (number % common_denominator) == 0: 
   print ("We found the number  %d  which can be divided by 7,13,15" % number)
   break
  else:
   number = randint(1, 1000000)



