"""
Write a python program that takes numbers in a loop
and for each number prints its square root
If value is negative or not a number show 
a warning and keep reading values
"""
import math

while True:
	print("Please enter your number: ")
	inputstr = raw_input()
	if inputstr == "":
		break
	try:
		number = float(inputstr)
	except Exception as e:
		print "Warning: The value is not a number. Error: " , e
		continue
	try:
		print "square root %f" % math.sqrt(number)
	except Exception as e:
		print "Warning: The value is a negative number. Error: " , e