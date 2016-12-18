import random

number = random.randint(1,101)

print "We choose a number between 1 to 100"

while True:
    guess = int(raw_input("Guess the number :"))
    if guess > number:
        print "Too high"
    elif guess < number:
        print "To low"
    elif guess == number: break

print "Correct ! This is the number !"
