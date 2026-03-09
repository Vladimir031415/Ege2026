def f(p):
    a.append(p+1)
    a.append(p+5)
    a.append(p*3)

a = [1]
for i in range(8):
    b = a[:]
    a = []
    for j in b:
        f(j)
cnt = 0
a = set(a)
for i in a:
    if i >= 1000 and i <= 1024:
        cnt+=1
print(cnt)