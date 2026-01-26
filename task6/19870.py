def ch(a):
    R = ""
    while a:
        R += str(a%4)
        a//=4
    return R[::-1]

r = []
for i in range(1,300):
    N = ch(i)
    if N[-1] in ["0", "2"]:
        N = "12" + N + ch(int(N[-1])*3)
    else:
        N = "13" + N + "21"
    if int(N, 4) > 50:
        r.append(int(N, 4))
print(min(r))
