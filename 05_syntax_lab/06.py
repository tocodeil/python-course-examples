from random import randint
rnd1=randint(1,11)
rnd2=randint(1,11)
for i in range(1,rnd1*rnd2+1,1):
    if i % rnd1 == 0 and i % rnd2 == 0:
        print "The 1st random number is {random1} \n The 2nd random number is {random2} \n The smallest devided number by both is {smallestDev}".format(random1 = rnd1,random2 = rnd2,smallestDev = i)
        break