"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""
print "Please enter lines:"
total_lines = ""
while True:
    line = raw_input()
    if len(line) == 0:
        break
    if len(total_lines) == 0:
        total_lines = line
    else:
        total_lines = line + '\n' + total_lines

if len(total_lines) == 0:
    print "No lines were entered"
else:
    lines_array = total_lines.splitlines()
    print "The lines in reverse order:"
    for i in range(len(lines_array)):
        print lines_array[i]