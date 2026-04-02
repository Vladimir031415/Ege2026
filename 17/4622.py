with open(r".\files\17_4622.txt") as file:
    data = [int(i) for i in file]


ans = []

m = min([x for x in data if x > 0 and x%19 == 0])
for i in range(len(data) - 1):
    num1, num2 = data[i: i + 2]
    if num1 + num2 <= m:
        ans.append(num1+num2)

print(len(ans))
print(max(ans))