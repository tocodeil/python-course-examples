""" Write a program that selects a random number
and asks the user to guess it.
After each guess print a hint "too large" or "too small" to the user.
Bonus: To make things interesting, the program should cheat once in a white
"""


import random

randomNumber = random.randint(1,100)

print "Guess the number (between 1 and 100):"

userNumber = -1

while True:
    userNumber = int(raw_input())

    cheatingFactor = random.randint(0, 100)
    if cheatingFactor % 11 == 0:
        print "*too large"
        continue
    elif cheatingFactor %12 == 0:
        print "*too small"
        continue

    if userNumber > randomNumber:
        print "too large"
    elif userNumber < randomNumber:
        print "too small"
    else:
        print "Bingo!"
        break


