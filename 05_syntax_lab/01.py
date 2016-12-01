"""
this program reads 10 numbers and prints the largest one - copied all
"""
maxnum = float('-inf')

for _ in range(10):
    num = float(raw_input())
    if num > maxnum:
        maxnum=num
print " Max Number is= %d"    % maxnum