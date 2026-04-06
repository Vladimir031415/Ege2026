with open(r"C:\Users\vova55555\Desktop\Ege2026\0probnik aprel\17.txt") as file:
    data = [int(i) for i in file]

m = max([i for i in data if len(str(i)) == 2])
print(m)
ans = []
for i in range(len(data)-1):
    if len(str(data[i])) == 2 or len(str(data[i+1])) == 2:
        if (data[i] + data[i+1])%m == 0:
            ans.append(data[i] + data[i+1])
print(len(data))
print(max(data))
