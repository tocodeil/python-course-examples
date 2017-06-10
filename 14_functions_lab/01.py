

def mysum(*args):
    res = 0
    for n in args:
        if type(n) is int:
            res += n
    return res


def mymul(*args):
    res = 1
    for n in args:
        if type(n) is int:
            res = n * res
    return res



print mysum(1, 2, "dwd")
print mymul(6, 5, "dwd")