
maxnum=float('-inf')
print"enter 10 numbers"
for _ in range(0,10):
    num = float(raw_input())
    if num > maxnum:
        maxnum = num

print maxnum


