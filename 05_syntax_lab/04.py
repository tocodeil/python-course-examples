"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""

lines = ""

while True:
    print ("Please enter you input: ")
    line = raw_input()
    lines = lines + line
    if not line: break

print ("The input was: " + lines[::-1])