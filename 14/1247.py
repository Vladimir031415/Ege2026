t = "0123456789ABCDEFGHIJK"


def Con(a, b):
    r = ""
    while a:
        r += t[a % b]
        a //= b
    return r[::-1]
a= Con(729**8 - 3**18 + 85, 9)
print(a.count("0"))