t = "0123456789ABCDEFGHIJK"


def Con(a, b):
    r = ""
    while a:
        r += t[a % b]
        a //= b
    return r[::-1]
r = []
for i in range(150):
    n = Con(i,3)
    if sum(map(int, n))%3==0:
        n += "212"
    else:
        n += Con((sum(map(int, n))%3)*2, 3)
    R = int(n,3)
    if R > 490:
        r.append(R)
print(min(r))
