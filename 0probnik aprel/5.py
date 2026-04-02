ans = []
def ch(a):
    r = ""
    while a:
        r += str(a%4)
        a //= 4
    return r[::-1]
for i in range(5, 100):
    N = ch(i)
    if N[-1] == "0":

        R = N + N[:2]
    else:
        R = N + ch(4 * int(N[-1]))
    R = int(R, 4)
    if R > 291:
        ans.append(R)
print(sorted(ans))



