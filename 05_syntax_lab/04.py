
myList = []

while True:
    txt = raw_input('Please enter something')
    if not txt:
        break
    else:
        myList.append(txt)


if myList:
    if len(myList) == 1:
        print myList
    else:
        print myList
        sorted_list = sorted(myList, reverse=True)
        print sorted_list
        for line in sorted_list:
            print line
