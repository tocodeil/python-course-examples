"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""


lines = ""
#print ("Please enter you input: ")

while True:
    line = raw_input()
    lines = line + '\n' + lines
    if not line: break

print ("\n" + lines[1::])


"""
# A similar idea but with a list

lines = []
while True:
    line = raw_input()
    lines.append(line)
    if not line: break

print lines[::-1]
"""