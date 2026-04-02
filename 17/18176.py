with open(r"C:\Users\vova1\PycharmProjects\Ege2026\17\files\17_18176.txt") as file:
    data = [int(i) for i in file]
ans = []
m = min([i for i in data if i > 0 and i%10 == 4])
for i in range(len(data) - 2):
    if sum(data[i:i+3]) == m:
        ans.append(sum(data[i:i+3]))
print(len(ans), max(ans))