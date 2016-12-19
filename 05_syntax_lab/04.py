"""
Write a program that reads lines from the user
until an empty line is entered.
After the user typed in an empty line,
print all previously entered lines in reverse
order (from last to first).
"""





print "Enter your text: "
i=0;
line = []
while True:
    string=raw_input()
    if len(string)>0:
        line.append(string)
        continue
    else: break
for l in range(len(line)-1, -1,- 1):
    print line[l]