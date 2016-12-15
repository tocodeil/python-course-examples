from random import randint

myNum1 = randint(1, 10)
myNum2 = randint(1, 10)

print myNum1
print myNum2
for x in range(1, 100):
    print x
    if x % myNum1 == 0 and x % myNum2 == 0:
        break
