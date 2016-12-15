import random

num = random.randint(1,100)
user = 0
while user != num:
    print 'guess the number'
    user = int(raw_input())
    if user > num:
        print 'too big man'
    elif user < num:
        print 'too small dude'
    else:break;

print 'bingo' , num