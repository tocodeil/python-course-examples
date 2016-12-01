"""
syntax_ex06.py

"""

from random import randint 


rand_num1 = randint(1, 10)
rand_num2 = randint(1, 10)
min_multiple = rand_num1*rand_num2
i=min_multiple
print " for those two numbers: ",rand_num1, ", " ,rand_num2

while i>=rand_num1 and i>=rand_num2:
    if i%rand_num1 + i%rand_num2 == 0:
        min_multiple = i
    i-=1

print " the smallest multiple is: ",min_multiple
