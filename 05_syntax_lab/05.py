import random

num = random.randint(1,1000000)
while num % 7 ==0 & num % 13 == 0 & num % 15 == 0:
    num = random.randint(1, 1000000)

print num