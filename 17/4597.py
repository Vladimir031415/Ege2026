with open(r".\files\17_4597.txt") as file:
    data = [int(i) for i in file]

m = min(data)
for i in range(len(data) - 1):
    nim1, num2 = data[i: i + 2]

