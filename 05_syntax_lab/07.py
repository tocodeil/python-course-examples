""" Write a program that selects a random number
and asks the user to guess it.
After each guess print a hint "too large" or "too small" to the user.
Bonus: To make things interesting, the program should cheat once in a white
"""

from random import randint

random_number = randint(1, 100)
print random_number
tries_allowed = 5

print "I'm thinking of a number between 1 and 100. You have 5 tries to guess it \n"

for guess in range(tries_allowed):
    user_input = int(raw_input("Please enter your guess"))
    if user_input > random_number:
        print "Please try harder. Your number is too high"

    elif user_input < random_number:
        print "Please try harder. Your number is too small"

    else:
        print "You did it. You guessed the number was " + str(random_number)
        break

else:
    print "You had 5 tries. I'm sorry, You are a failure"