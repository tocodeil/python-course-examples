import sys

if len(sys.argv) != 3:
    raise 'You need to pass 2 arguments'

myNum1 = sys.argv[1]
myNum2 = sys.argv[2]

if not myNum1.isdigit() or not myNum2.isdigit():
    raise 'please type a digit for parameters'
    exit
else:
    newNum = int(myNum1) + int(myNum2)
    print 'Sum of args = {num}'.format(num=newNum)