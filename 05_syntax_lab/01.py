""" read 10 numbers from user and print the bigger one"""
max = -100000
print "insert 10 nubers:"
for i in range(10):
    x = raw_input()
    if int(x) > max:
        max = int(x)
print "the bigest number is:", max