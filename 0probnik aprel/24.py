with open(r"C:\Users\vova55555\Desktop\Ege2026\0probnik aprel\24.txt") as file:
    data = file.readline()
a = list(map(len, data.split("Z")))
r = []
for i in range(len(a)-269):
    r.append(sum(a[i: i + 269]))
print(min(r) + 270)