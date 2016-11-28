"""
Write a program that generates random integers in a loop
until it finds a number that is divisible by: 7, 13, and 15.
"""



from random import randint

while True:
    random_number= randint(1,1000000)
    print random_number
    if random_number%7 != 0: continue
    elif random_number%13 !=0 : continue
    elif random_number%15 != 0 : 
        continue
    else:
         break
print ("I found a magic number!!!")
