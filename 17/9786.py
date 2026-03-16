with open(r".\files\17_9786.txt") as file:
    data = [int(i) for i in file]


ans = []

m = max([x for x in data if abs(x)%100 == 25])
for i in range(len(data) - 2):
    num = data[i: i + 3]
    if not all(abs(i)//1000 < 10 for i in num):
        if sum(num) <= m:
            ans.append(sum(num))


print(len(ans))
print(max(ans))