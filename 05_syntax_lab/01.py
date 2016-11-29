"""
 This code is getting 10 numbers and printing out the biggest.
"""

number = 0
bignumber = 0 
oldnumber = 0
i = 0
print ("Enter 10 decimal numbers") 
for i in range (1,10):
    number = int(raw_input())
    if (number > bignumber ) :
      bignumber = number
    
print ("The final biggest number is", bignumber)
        

        
