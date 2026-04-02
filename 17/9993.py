def p(a):
    if a < 2: return False
    return all(a % i != 0 for i in range(2, int(a ** 0.5) + 1))


with open(r".\17_9993") as file:
    data = [int(i) for i in file]

mx = max(i for i in data if abs(i) % 100 == 17)
ans = []
for num in zip(data, data[1:]):
    