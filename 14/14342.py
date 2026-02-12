from string import printable
a = printable
def w(v,p):
    R = 0
    t = 0
    for i in v[::-1]:
        R += (a.index(i)+1) * (p ** t)
        t += 1
    return R


for p in range(20, 37):
    if w("bo",p) + w("om", p) + w("bl", p) == w("cng", p):
        print(p)