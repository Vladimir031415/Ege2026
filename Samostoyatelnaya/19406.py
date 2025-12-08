from string import printable
def tf(a):
    a = str(a)
    u = []
    for i in printable:
        u.append(a.count(i))
    e = max(u)
    return int(printable[u.index(e)])



for i in printable[:35]:
    n1 = int(f"6{i}QR{i}", 35)
    n2 = int(f"{i}59SH", 35)
    n3 = int(f"PH{i}69YW", 35)
    if (n1+n2+n3)%(tf(n1+n2+n3)**2) == 0:
        print((n1+n2+n3)/(tf(n1+n2+n3)**2))
        break