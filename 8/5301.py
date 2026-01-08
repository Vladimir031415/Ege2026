from itertools import product
cnt = 0
for i in product("LESAP", repeat=5):
    i = "".join(i)
    if i[0] != "P" and i[4] != "P" and i.count("P") == 1:
        if ("EA" not in i) and ("LS" not in i) and ("SS" not in i) and("LL" not in i) and ("EE" not in i) and("AA" not in i) :
            cnt += 1
print(cnt)