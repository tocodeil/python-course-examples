import random

num_a = random.randint(1,10)
num_b = random.randint(1,10)
lst = []

for x in range(1,num_a*num_b+1):
    if x % num_a == 0:
        if x % num_b == 0:
            lst.append(x)

print "The numbers are %s and %s" % (num_a,num_b)
print "The lowest common denominator : %s" % (min(lst))
