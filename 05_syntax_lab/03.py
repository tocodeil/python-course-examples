import random

rand_num = random.randint(1,10001)

rand_num = str(rand_num)
sum_num = 0

for i in range(len(rand_num)):
    sum_num = sum_num + int(rand_num[i])

print "The random number is : %s" % (rand_num)
print "The sum of his digits : %s " % (sum_num)
