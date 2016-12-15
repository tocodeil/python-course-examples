import sys
sum = float(0)
if len(sys.argv) == 3:
    try:
        sum = float(sys.argv[1]) + float(sys.argv[2])
        print "The sum of both args is {arg}".format(arg=sum)
    except ValueError:
        print "Error, Please input valid numbers"
else:
    print "Error, please input 2 args"
