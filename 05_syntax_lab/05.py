from random import randint
x = True
while x: 
    num = randint(1,1000000)    
    if num % 7 == 0 and num % 13 == 0 and num % 15 == 0: break
print "the number %d devides in  7, 13, 15" % num