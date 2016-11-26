import random
kfula = 0
num1 = random.randint(1,10)
num2 = random.randint(1,10)
if num1 > num2:
    kfula = num1
    while kfula % num1 != 0 or kfula % num2 != 0:
        kfula+=1
else:
        kfula = num2
        while kfula % num1 != 0 or kfula % num2 != 0:
            kfula += 1
print num1,num2
print kfula
