with open("ans.txt", "w") as f:
    data = [list(map(int, i.split())) for i in data]
cnt = 0
for i in data:
    n = [i.count(j) for j in i]
    if sorted(n) == [1,1,1,2,2]:
        s1 = [j for j in i if i.count(j) == 1]
        s2 = [j for j in i if j % 2]
        if s1 <= s2:
            cnt += 1
