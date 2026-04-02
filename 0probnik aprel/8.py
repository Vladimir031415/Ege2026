from itertools import product


cnt = 0
for i in product("0123456", repeat=7):
    i = "".join(i)
    if int(i[0]) not in [0, 3, 5] and not("22" in i and "44" in i):
        cnt += 1

print(cnt)
print(7**6 * 6)