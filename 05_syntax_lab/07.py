""" Write a program that selects a random number
and asks the user to guess it.
After each guess print a hint "too large" or "too small" to the user.
Bonus: To make things interesting, the program should cheat once in a white
"""
print "Try to guess my number (between 1 to 100)"
from random import randint
num = randint(1, 100)
while True:
 guess = raw_input()
 if int(guess) > num:
  print "Too high, try again"
 elif int(guess) < num:
  print "Too low, try again"
 else:
  print "Bingo !!!"
  break

