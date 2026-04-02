with open(r"C:\Users\vova55555\Desktop\Ege2026\0probnik aprel\26.txt") as file:
    data = [list(map(int, i.split())) for i in file]
tchk = []
ts = []
for s_t in data:
    s = s_t[0]
    t = s_t[1]
    if t in tchk:
        for i in range(len(ts)):
            if t == ts[i][0]:
                ts[i].append(s)
    else:
        tchk.append(t)
        ts.append([t,s])
pr = []
for i in ts:
    if len(i) >= 5:
        pr.append(i)
ans = []
for i in pr:
    sp = sorted(i[1:])
    n = 1
    for j in range(len(sp)-1):
        if sp[j+1]-sp[j-1] == 1:
            n += 1
        else:
            n = 1
    ans.append([n, i[0]])
print(sorted(ans))





