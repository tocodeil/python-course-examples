#!/usr/bin/python
global_c = 1
class MyCounter:
  def __init__(self):
    global global_c
    self.count = global_c
    global_c += 1





for _ in range(10):
     c1 = MyCounter()

# should print 10
print MyCounter.count
