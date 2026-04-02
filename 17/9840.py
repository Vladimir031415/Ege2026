with open(r".\files\17_9840.txt") as file:
    data = [int(i) for i in file]


ans = []

m = max([x for x in data if abs(x)%100 == 39 and abs(x)//1000 < 10])
for i in range(len(data) - 1):
    num1, num2 = data[i: i + 2]
    if not ((num1 // 1000 < 10) == (num2 // 1000 < 10)):
        if (num1 + num2)**2 <= m**2:
            ans.append(num1 + num2)


print(len(ans))
print(max(ans))