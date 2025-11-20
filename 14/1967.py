
t = "0123456789ABCDEFGHIJK"


def Con(a, b):
    r = ""
    while a:
        r += t[a % b]
        a //= b
    return r[::-1]


num = 51*7**12-7**3-22

print(sum(map(lambda x: int(x,32),(Con(num,16)))))