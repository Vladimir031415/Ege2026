with open(r".\files\17_4597.txt") as file:
    data = [int(i) for i in file]


ans = []

m = min(data)
for i in range(len(data) - 1):
    num1, num2 = data[i: i + 2]
    if num1 % 117 == m or num2 % 117 == m:
        ans.append(num1+num2)

print(len(ans))
print(max(ans))


