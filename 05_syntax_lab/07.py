""" Write a program that selects a random number
and asks the user to guess it.
After each guess print a hint "too large" or "too small" to the user.
Bonus: To make things interesting, the program should cheat once in a white
"""
import random
a = random.randint (1,100)
print a
print "Please guess what is my number(1-100)?"
guess = int(raw_input())
while guess != a:
    if guess > a:
        print "Your guess is bigger than my number"
        print "Please guess again what is my number?"
        guess = int(raw_input())
    if guess < a:
        print "Your guess is smaller than my number"
        print "Please guess again what is my number?"
        guess = int(raw_input())
print "WOW!" + str(guess) + " is really my number!"






