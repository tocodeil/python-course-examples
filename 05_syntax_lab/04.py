line_list = []

line = raw_input("Please enter a line :")
while len(line) > 0:
    line_list.append(line)
    line = raw_input("Enter another line :")
else:
    for item in line_list[::-1]:
        print item