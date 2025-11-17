def S(a,b):
    r = ""
    while a:
        r += str(a%b)
        a//=b
    return r[::-1]
for i in range(8,30):
    e = S(i,2)
    if i%8 == 0:
        e = e + e[-2:]
    else:
        e = e + S((i%8)*2,2)
    print(i, int(e, 3))
