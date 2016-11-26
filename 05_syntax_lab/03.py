import random
sum = 0
num = random.randint(1,10000)
#print num
while num != 0:
    sum += num % 10
    num /=10

print sum