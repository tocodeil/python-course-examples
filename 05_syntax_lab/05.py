import random

number = random.randint(1,1000001)

while number % 7 != 0 or number % 13 != 0 or number % 15 != 0:
    number = random.randint(1, 1000001)
else:
    print number

