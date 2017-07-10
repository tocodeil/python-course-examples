""" get string from user and return the in reverse"""
x = raw_input()
y = x
i=0
while x != "":
    i +=1
    x = raw_input()
    y += ' '
    y += x
    xi = x
print y [::-1]
