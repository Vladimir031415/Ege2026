with open(r"C:\Users\vova1\PycharmProjects\Ege2026\9\files\7030.txt") as file:
    data = [list([map(int, i.split())]) for i in file]
print(data[0])
cnt = 0
for b in data:
    p = [b.count(i) for i in b]
    #print(b)
    #print(p)
    if sorted(p) == [2,2,2,2,2,2]:

        a = sorted(set(b))[0]**2
        if a[0]**2 + a[1]**2 == a[2]**2:
            cnt += 1
print(cnt)

