def f(a):
    R = ""
    while a:
        R += str(a%3)
        a//=3
    return R[::-1]
d = []
for i in range(1,300):
    R = f(i)
    if R[-1] == "0":
        R += R[-2:]
    else:
        R += f(sum(map(int, R))*3)
    R = int(R,3)
    if R > 203:
        d.append(R)
print(d)
print(min(d))



