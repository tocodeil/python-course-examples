import random

number = random.randint(1,101)

print "We choose a number between 1 to 100"
guess = int(raw_input("Guess the number :"))

while guess != number:
    if guess > number:
        guess = int(raw_input("Too high.. Try again :"))
    elif guess < number:
        guess = int(raw_input("Too low.. Try again :"))

print "Correct ! This is the number !"

