import random

num_a = random.randint(1,10)
num_b = random.randint(1,10)
num_list = []

for x in range(1,num_b+1):
    if num_a*x % num_b == 0:
        num_list.append(num_a*x)

print min(num_list)
