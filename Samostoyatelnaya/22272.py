def p(a):
    r = ""
    while a:
        r += str(a%9)
        a //= 9
    return r[::-1]
a = []
for i in range(1,200):
    N = p(i)
    if N[0] == "7":
        N.replace("6", "*")
        N.replace("3", "6")
        N.replace("*", "3")
        N = "34" + N
    else:
        N = "3" + N[1:] + "45"
    R = int(N, 9)
    if R < 2876:
        a.append(R)
Rm = max(a)
for i in range(1,200):
    N = p(i)
    if N[0] == "7":
        N.replace("6", "*")
        N.replace("3", "6")
        N.replace("*", "3")
        N = "34" + N
    else:
        N = "3" + N[1:] + "45"
    R = int(N, 9)
    if R == Rm:
        print(i)
