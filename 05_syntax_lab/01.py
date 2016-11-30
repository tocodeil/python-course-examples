maxnum = float('-inf')

for _ in range(10):
    num = float (raw_input())
    if num > maxnum:
        maxnum = num
    print "max number = %f" % maxnum