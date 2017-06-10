def mysum(*args):
    res = 0
    for n in args:
        if type(n) is int:
            if n > 10:
                ten = n/10
                num = ten % 10
                res += num
        else:
            raise "ONLY integer can be added as argument"
    return res


print mysum(1113, 3223, 1244, 34595)
print mysum(1, 2, "dwd")