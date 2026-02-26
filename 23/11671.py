def f(p):
    a.append(p+10)
    a.append(p-5)
a = [1]
for i in range(15):
    b = a[:]
    a = []
    for j in b:
        f(j)
print(len(set(a)))