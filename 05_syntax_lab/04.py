"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""

print("Enter line")

userInput = raw_input()
output = []

while userInput:
	output.append(userInput)
	userInput = raw_input()
	
output.reverse()

for line in output:
	print(line)

	