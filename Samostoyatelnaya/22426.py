a = 7**270 + 7**170 + 7**70
t = []
for i in range(1,10000):
    m = a - i
    n = 0
    while m:
        if m % 7 == 0:
            n+=1
        m//=7
    t.append(n)
print(max(t))

