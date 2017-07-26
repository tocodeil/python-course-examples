#!/usr/bin/python
def mysum(*nums):
	s = 0
	for i in nums:
		try:
			s += int(i)
		except:
			pass
	return s
	

def mymul(*nums):
	s = 1
	for i in nums:
		try:
			s = s * int(i)
		except:
			pass
	return s	

print mymul(12 , 1 , 2 ,'asdas')