def t(a):
    r = ""
    while a:
        r += str(a%39)
        a //= 39
    return r[::-1]
ans = []
for x in range(1, 9431):
    ans.append(t(39**483 + 39**235 - x).count("0"))
print(list(sorted(set(ans))))


