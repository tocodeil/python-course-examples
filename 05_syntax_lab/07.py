""" Write a program that selects a random number
and asks the user to guess it.
After each guess print a hint "too large" or "too small" to the user.
Bonus: To make things interesting, the program should cheat once in a white
"""
from random import randint

num = randint(1,100)
print num
print "Try to guess number!"
guessed = False


while(guessed != True):
    guessedNum = int(raw_input())
    if(guessedNum == num):
        print "That's it!'"
        guessed = True
    elif(guessedNum > num):
        print "Too big!"
    else:
        print "Too small!"