""" 
The program selects a random number
and asks the user to guess it.
After each guess the program prints a hint "too large" or "too small" to the user.

"""
import random

num = random.randrange(100)

while True:
  print "Please enter your guess:"
  UserNum = int(raw_input())
  if num == UserNum:
    print "Excellent you are right, the number is:" ,num
    break
  elif num > UserNum:
	  print "Too small"
  else :  
	  print "Too big"
