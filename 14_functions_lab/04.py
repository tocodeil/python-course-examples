def longer_than(length, *kwords):
    for n in kwords:
        if type(n) is not str:
            raise "ONLY str is allowed"

        if len(n) > length:
            print n
    return


#print longer_than(2, "lionel", "david", "oo")
print longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time')
