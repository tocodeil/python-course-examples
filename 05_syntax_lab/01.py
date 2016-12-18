"""
# Enter 10 numbers in a row (with blank space between them)
#Any other format will ask for a fix

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

"""

# Enter 10 numbers one by one
# Any other value will cause ValueError and it fails

num_list = []

for item in range(10):
    item = float(raw_input("Enter number >"))
    num_list.append(item)

print max(num_list)
