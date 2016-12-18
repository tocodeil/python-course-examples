import random

num_list = []

for num in range(7):
    num_list.append(random.randint(1,101))

sum_list = sum(num_list)

print "The sum of 7 random number is %s" % (sum_list)
if sum_list % 7 == 0:
    print "BOOM !"

