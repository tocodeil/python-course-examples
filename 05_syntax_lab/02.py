total = 0
from random import randint
for i in range(7):
    total += randint(1, 101)

if total % 7 == 0:
    print "The total is {}, BOOM!".format(total)
else:
    print "The total is {}".format(total)
    
