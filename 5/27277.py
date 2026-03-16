def f(x):
    r = ""
    while x:
        r = r + str(x%3)
        x = x//3
    return r[::-1]
a = []
for N in range(9,100):
    R = f(N)
    if R[-1] != "0":
        R = "1" + R + R[3:]
    else:
        R = R + f(sum(map(int, R)) * 8)
    a.append(int(R, 3))

b = []
for i in a:
    b.append(abs(i-1200))

bm = min(b)
Rm = a[b.index[bm]]
print(Rm)
#b = list(map(abs, map(-1220, a)))
#bm = min(b)
#Rm = a[b.index[bm]]

