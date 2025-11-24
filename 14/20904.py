def Con(a, b):
    r = ""
    while a:
        r += str(a % b)
        a //= b
    return r[::-1]

for x in range(1,2031):
    s = Con(3**100 - x, 3)
    if s.count("0") == 1:
        print(x)

