"""
This code is random number in range of 1-10000 and cala the sum of the number's' digits
"""
x = 0
i = 10
random = 0
reminder = 0
divider = 1000
reminder = 0
from random import randint
randomnum = randint (1,10000)
print randomnum
for i in range (1,5,1):
    x = randomnum / divider
    reminder += x
    randomnum = randomnum % divider
    divider  = divider/10 
print (" The sum of the number is", reminder )
      
