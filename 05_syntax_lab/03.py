import random

rand_num = random.randint(1,10000)

rand_num = str(rand_num)
sum_num = 0

for c in rand_num:
    sum_num = sum_num + int(c)

print "The random number is : %s" % (rand_num)
print "The sum of his digits : %s " % (sum_num)
