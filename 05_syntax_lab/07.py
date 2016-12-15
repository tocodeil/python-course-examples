
"""
This code is random number in range of 1-100 and let the user to guess by prining high/low number, until the user hits
Phase B: add random to the high/low prints so it will be harder to guess the number  
"""



from random import randint
random = randint (1,100)

user_input = int(raw_input('User enter number between 1-100\r\n'))
while True:
 if user_input == random:
     print ("very good : The number you entered is %d and the randon number is %d" % (user_input , random))
     break
 elif user_input > random:
     print "too high number, continue entering numbers"
     user_input = int(raw_input('User enter number between 1-100\r\n'))
 elif   user_input < random:
    print "Too low number, continue entering numbers"
    user_input = int(raw_input('User enter number between 1-100\r\n'))

     

    
