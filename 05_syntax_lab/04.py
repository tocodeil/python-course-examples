

"""
 This code is reading user input (followed by CR) and if thers is empty line ,the code will print the entered number in reversed order 
"""

chars = s = ''
chars = raw_input('Enter numbers - for ending  just press Enter without any numbers \r\n')
while  ( chars != ''):
    s=chars+'\r'+s
    chars = raw_input()
    s =  s.replace('\r','\n')
print s
