#!/usr/bin/python
def longer_than(l , *words):
	return [word for word in words if len(word) > l]

print longer_than(3, '2312321', '213sadsad' , '2123', '213' '222' ,'22')