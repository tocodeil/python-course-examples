from random import randint

myList = []
for x in range(0, 7):
    myList.append(randint(1, 100))

result = sum(myList)
print myList
print result

if result % 7 == 0:
    print 'boom'
