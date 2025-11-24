def Con(a, b):
    r = ""
    while a:
        r += str(a % b)
        a //= b
    return r[::-1]
a = []
for x in range(1,3001):
    s = Con(4**210 + 4**110 - x, 4)
    a.append(s.count("0"))

