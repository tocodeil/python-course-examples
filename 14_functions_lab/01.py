"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""

def mysum(*numbers):
    totalsum=0
    vaildigits=[]
    for i in numbers: 
        if (type(i)==int or type(i)==float):
            vaildigits.append(i) 
            print vaildigits
            totalsum+=i
    return totalsum


print mysum(5,'o',-5,2)

def mymul (*numbers):
    vaildigits=[]
    for i in numbers: 
        if (type(i)==int or type(i)==float):
            vaildigits.append(i)     
            mul=reduce(lambda x,y:x*y,vaildigits)
    return mul

print mymul(-1,9,10,10)

