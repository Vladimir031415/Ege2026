def Con(a, b):
    r = ""
    while a:
        r += str(a % b)
        a //= b
    return r[::-1]


num = 51*7**12-7**3-22
print(sum(map(int,(Con(num,7)))))

