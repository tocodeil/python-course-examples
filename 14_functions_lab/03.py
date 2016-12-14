"""
Write a function called "sum_tens" that calculates the sum
of the 10th digit from all arguments passed to it
"""


def sum_tens(*numbers):
 numberslist = list(numbers)
 i=''
 sum1=0
 tendigit=0
 for index in range(len(numberslist)):
   i = str(numberslist[index])
   if len(i)>=2:
     tendigit = int(i[-2])
     sum1 +=tendigit   
 return sum1
       
  


  
print sum_tens (111,-222,333,3,12345,0,20,122) 
