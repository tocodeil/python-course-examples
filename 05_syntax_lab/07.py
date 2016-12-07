from random import randint
rnd=randint(1,101)
usrpick = 0
while True:
    print "Please enter your guess..."
    usrpick = int(raw_input())
    if usrpick > rnd:
        print "Too high..."
        continue
    if usrpick < rnd:
        print "Too low..."
        continue
    else:
        print "BINGO!!!"
        break;


