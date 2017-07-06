print "Input 10 numbers. The code will output the largest."
   
maxnum = float('-inf')

for i in range(10):
    num = int(raw_input())
    if num > maxnum:
        maxnum = num

print "Max number = %d" %maxnum