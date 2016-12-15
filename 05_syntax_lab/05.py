from random import randint

while True:
    myNum = randint(1, 1000000)
    if myNum % 7 == 0 and myNum % 13 == 0 and myNum % 15 == 0:
        print myNum
        break
    else:
        print myNum
