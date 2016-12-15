"""m
Write a class called MyCounter that counts
how many times it was initialised, so the
following code:

    for _ in range(10):
        c1 = MyCounter()

    print MyCounter.count

should print 10
"""

class MyCounter (object):
	count = 0
	
	def __init__(self):
		MyCounter.count += 1