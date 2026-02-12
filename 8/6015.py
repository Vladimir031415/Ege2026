from itertools import product
cnt = 0
for i in product("012345678", repeat=7):
    i = "".join(i)
    if i[0] != "0":
        if i.count("8")==0:
            if int(i[0])%2 == 0 and int(i[-1])%2 == 1:
                cnt += 1
print(cnt)
