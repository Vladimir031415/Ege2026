cnt = 0
from itertools import product
for i in product("01", repeat=14):
    i = "".join(i)
    if (i.count("1") + 7) % 5 != 0:
        cnt += 1
print(cnt)
print(cnt*5/4)
print(2**14)