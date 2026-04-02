with open(r"C:\Users\vova1\PycharmProjects\Ege2026\17\files\17_15333.txt") as file:
    data = [int(i) for i in file]
ans = []
m = max([i for i in data if i%19 == 0])
for i in range(len(data) - 1):
    if data[i] >= m or data[i+1] >= m:
        ans.append(data[i] + data[i+1])
print(len(ans), max(ans))