""" Write a program that selects a random number
and asks the user to guess it.
After each guess print a hint "too large" or "too small" to the user.
Bonus: To make things interesting, the program should cheat once in a white
"""


from random import randint 

num=randint(1,100)

while True:
    print "Please guess a number between 1 and 100: "
    guess = int(raw_input())
    if guess > num:
        print "The number you guessed is bigger than the right number"
    elif guess < num:
        print "The number you huessed is smaller than the right number"
    elif guess == num:
        print "You are right!!!"
        break
    print num
print "Game over"
