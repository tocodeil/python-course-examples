"""
syntax_ex03.py

"""
from random import randint 

i = 0
lucky_num_dig_sum = 0
lucky_num = randint(1, 10000)
print lucky_num
while i < len(str(lucky_num)):
    lucky_num_dig_sum += int(str(lucky_num)[i])
    i+=1

print "All numbers summarized to : " ,lucky_num_dig_sum

