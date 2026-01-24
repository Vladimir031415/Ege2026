def s(a):
    R = ""
    while a:
        R += str(a%7)
        a//=7
    return R[::-1]

print(sum(map(int, list(s(5*343**2031 + 4*49**2142 - 3*7**111 + 7**222)))))