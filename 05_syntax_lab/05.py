import random

while True:
    number = random.randint(1, 1000001)
    if number % 7 == 0 and number % 13 == 0 and number % 15 == 0:
        print number
        break
