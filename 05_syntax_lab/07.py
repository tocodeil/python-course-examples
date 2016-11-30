""" Write a program that selects a random number
and asks the user to guess it.
After each guess print a hint "too large" or "too small" to the user.
Bonus: To make things interesting, the program should cheat once in a white
"""
import random
x = random.randint(1,100)
num = int(raw_input())
print num
while (num != x):
    if num > x:
     print "you choose large number, please choose again:"
     num = int(raw_input())
    elif num < x :
       print "you choose smaller number, please choose again"
       num = int(raw_input())

print "you choose the same number"


