import sys


myNum = sys.argv[1]
if not myNum.isdigit():
    print 'please type a digit as parameter'
    exit
elif int(myNum) == 0:
    exit
else:
    for x in range(0, int(myNum)):
        print 'Hello Python'
