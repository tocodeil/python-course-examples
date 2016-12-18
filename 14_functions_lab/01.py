"""
Write 2 functions:
    mysum - returns the sum of its input arguments
    mymul - returns the multiplication of its input arguments
    Ignore non-numeric arguments
"""

def mysum(*numbers1):
    totalsum=0
    vaildigits=[]
    for i in numbers1: 
        if type(i)==int:
            vaildigits.append(i) 
        for i in vaildigits:
            totalsum+=i
        return totalsum


print mysum(5,5,'a',1)

def mymul (*numbers):
 vaildigits=[]
 for i in numbers: 
  if type(i)==int:
   vaildigits.append(i)     
   mul=reduce(lambda x,y:x*y,vaildigits)
 return mul

print mymul(1,9,10,'j')

