user_list = []

lst = raw_input("Enter here 10 numbers :")
while len(lst.split()) != 10:
    for each in lst.split():
        if each.isdigit() != True:
            lst = raw_input("Please enter numbers only:")
    print "Exacly 10 numbers please"
    lst = raw_input("Here.. Try again:")

for each in lst.split():
    if each.isdigit() != True:
        lst = raw_input("Please enter numbers only:")
else:
    for item in lst.split():
        item = int(item)
        user_list.append(item)


print max(user_list)