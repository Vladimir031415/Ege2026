def Con(a, b):
    r = ""
    while a:
        r += str(a % b)
        a //= b
    return r[::-1]

for x in range(1,3000):
    s = Con(9**150 + 9**30 - x, 9)
    if s.count("0") == 122:
        print(x)