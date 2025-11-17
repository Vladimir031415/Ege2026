for i in range(10000, 100000):
    a = max(map(int, str(i)))
    b = min(map(int, str(i)))
    c = (a + b) ** 2
    d = 1
    for u in str(i):
        if int(u) % 2 == 0:
            d *= int(u)
    g = [c, d]
    h = int(str(max(g)) + str(min(g)))
    if h == 12116:
        print(i)
        break
