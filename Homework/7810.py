from itertools import product

cnt = 0
for i in product("MASLO", repeat=6):
    i = "".join(i)
    if i.count("O") + i.count("A") == 1:
        cnt += 1
print(cnt)