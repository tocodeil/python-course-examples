""" Write a program that selects a random number
and asks the user to guess it.
After each guess print a hint "too large" or "too small" to the user.
Bonus: To make things interesting, the program should cheat once in a white
"""
from random import randint

number = randint(1, 100)
print "Please guess which number, between 1-100, I was thinking of?"

while True:
    guess = int(raw_input())
    revert_answer = randint(1, 100) > 80
    if guess == number:
        print "You are right!!!"
        break
    elif guess < number:
        if revert_answer == True:
            print "Too large. Try again..."
        else: 
            print "Too small. Try again..."
    elif revert_answer == True:
        print "Too small. Try again..."
    else:
        print "Too large. Try again..."
 
