
num_inserted = 0
myList = []
while num_inserted != 10:
    print 'Please add an additional number, up to 10'
    num_temp = raw_input()
    while not num_temp.isdigit():
        print 'Please type a digital number'
        num_temp = raw_input()
    myList.append(int(num_temp))
    num_inserted += 1

print max(myList)
