x=0
count=0
from random import randint
x=[randint(1,100) for p in range(0,7)]
count=  sum(x)
print  x
print count

test=float(count)/7
print "Test ufter deviding: ", test
if test.is_integer():
    print "Boom !!!!!!!!!!!!!!!!!!!!"
else:
    print "not Boom"
