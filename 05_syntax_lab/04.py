"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""
x= ''
line = raw_input()
while line:
    if line != '\n':
        x = line +'\n'+ x
    line = raw_input()
    if not line:
        break

print x
