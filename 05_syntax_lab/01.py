"""
 This code is getting 10 numbers and printing out the biggest.
"""
number = float('-inf')
bignumber = float('-inf')
print ("Enter 10 decimal numbers")
for _ in range(10):
    number = float(raw_input())
    if (number > bignumber ) :
         bignumber = number 
print ("Max number = %f" % bignumber)

