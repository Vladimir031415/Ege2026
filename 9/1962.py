with open(r"1962.txt") as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for i in data:
    s = sorted(i)
    if s[0] + s[1] >= s[2]: cnt += 1
print(cnt)