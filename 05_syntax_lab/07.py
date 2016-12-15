from random import randint

myNum = randint(1, 100)
print myNum

while True:
    user_num = raw_input('Please guess the number')
    if int(user_num) > myNum:
        if randint(1, 20) == 5:
            print 'Number typed is too Small'
        else:
            print 'Number typed is too big'
    if int(user_num) < myNum:
        if randint(1, 20) == 5:
            print 'Number typed is too Big'
        else:
            print 'Number typed is too small'
    if int(user_num) == myNum:
        print 'Good Guess!!!!'
        break
