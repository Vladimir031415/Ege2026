t = "0123456789ABCDEFGHIJK"


def Con(a, b):
    r = ""
    while a:
        r += t[a % b]
        a //= b
    return r[::-1]
a= Con(283**382 + 9**15 + 2**3, 14)
print(a.count("B")-a.count("C"))