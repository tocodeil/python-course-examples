"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""

result = ""
input = raw_input()

while(input != ""):
    result = "{0}{1}{2}".format(input, "\n", result)
    input = raw_input()

print(result)
