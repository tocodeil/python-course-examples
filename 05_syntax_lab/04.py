inputList = []
print "please enter sentence:"
line = raw_input()
inputList.append(line)

while len(line) > 0:

    print "please enter sentence:"
    line = raw_input()
    inputList.append(line)

inputList.reverse()
for sentences in inputList:
    print sentences
