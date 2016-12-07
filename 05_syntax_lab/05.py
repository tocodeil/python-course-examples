from random import randint
rnd=0
while True:
    rnd = randint(1,1000000001)
    if rnd % 15 == 0 and rnd % 13 == 0 and rnd % 7 == 0:
        print "The random number is {random}, and it devided by 15,13 and 7.".format(random = rnd)
        break
    else: continue


