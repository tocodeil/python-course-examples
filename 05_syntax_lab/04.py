line_list = []

while True:
    line = raw_input("Enter another line :")
    if len(line) > 0:
        line_list.append(line)
    else:
        break
for item in line_list[::-1]:
    print item
