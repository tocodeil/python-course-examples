total = 0
from random import randint
rnd = str(randint(1,10001))
for i in rnd:
    total += int(i)

print "The random number is {random}, the sum of its digits is {sum}".format(random = rnd, sum = total)