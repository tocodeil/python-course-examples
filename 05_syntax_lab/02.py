import random

for _ in range(0,7):
    num = random.randint(1,100)
    if num % 7 == 0:
        print num, 'boom'
