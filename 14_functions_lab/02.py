

def mysum(first, second):
    if type(first) is not int:
        print "argument {arg} should be integer".format(arg=first)
        raise
    if type(second) is not str:
        print "argument {arg} should be string".format(arg=second)
        raise
    return


#print mysum(11, 32)
print mysum(1, "dwd")
