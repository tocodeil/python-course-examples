biggestNum = float(raw_input())

for i in range(9):
    print "please enter number:"
    userNum = float(raw_input())
    if biggestNum < userNum :
        biggestNum = userNum

print 'The Largest number is:', biggestNum
