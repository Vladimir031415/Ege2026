def t(a):
    R = ""
    while a:
        R += str(a%3)
        a //= 3
    return R[::-1]
def s(a):
    R = 0
    for j in a:
        R += int(j)
    return(R)

S = []
for i in range(100):
    N = t(i)
    if s(N) % 2 == 0:
        R = "1" + N + "2"
    else:
        R = "2" + N + "0"
    R = int(R, 3)

    S.append(R)
print(S)
print(min(S))

