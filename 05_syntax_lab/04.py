"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""
print "Please enter lines:"
lines = []
while True:
    line = raw_input()
    if len(line) == 0:
        break
    lines.append(line)

if len(lines) == 0:
    print "No lines were entered"
else:
    print "The lines in reverse order:"
    for item in lines[::-1]:
        print item