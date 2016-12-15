
""" 
 Use range() and list comprehension to get 
 the list of all lowercase english letters 
 Hint: look for chr() and ord() 
 """ 


allchars=''
finalist= []
for i in range(1,254):
 allchars +=str(chr (i))

ABClist = set('abcdefghijklmnopqrstuvwxyz')

finalist  += [char for char in allchars if (char in ABClist)]
print  finalist
 