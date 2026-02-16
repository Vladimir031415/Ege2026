from itertools import product
alf = "0123456"
cnt = 0
for i in product(alf, repeat=6):
    i = "".join(i)
    if "316" in i:
        cnt += int(i, 7) + 1
print(cnt)