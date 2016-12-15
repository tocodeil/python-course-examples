from random import randint

myNum = randint(1, 1000)
myList = []

for ch in str(myNum):
    #print ch
    myList.append(int(ch))

print sum(myList)

