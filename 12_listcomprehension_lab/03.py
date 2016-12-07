from collections import Counter


for i in range(97, 123):
    txt = chr(i)
    for k in range(97, 123):
        if len(txt) == 1:
            txt += chr(k)
        else:
            txt = txt[:1] + chr(k) + txt[1:]
        for j in range(97, 123):
            if len(txt) == 2:
                txt += chr(j)
            else:
                txt = txt[:2] + chr(j)
            if Counter(txt)[chr(i)] == 2 or Counter(txt)[chr(i)] == 3:
                print txt

