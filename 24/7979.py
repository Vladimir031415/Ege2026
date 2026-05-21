from re import *

with open(r"C:\Users\vova55555\Desktop\Ege2026\24\24-314.txt") as file:
    data = file.readline()

num = "([1-7][0-7]*|0)"
pat = fr"F({num}[+*])+{num}"

matches = [match.group() for match in finditer(pat, data)]
res = []
for i in matches:
    i = i[1:]
    sts = []
    st = ""
    for j in i:
        if j in "+*":
            sts.append(str(int(st, 8)))
            st = ''
            sts.append(j)
        else:
            st += j
    sts.append(str(int(st, 8)))
    res += [[len(i), eval("".join(sts))]]

print(max(res)[1])



