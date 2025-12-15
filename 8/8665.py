from itertools import permutations, combinations, product

cnt = 0
for pos, val in enumerate(product("0123456789AB" , repeat=5)):

    val = "".join(val)
    if val.count("B")==2 and val[0] != "0":

        d = ""
        for i in val:
            if int(i,12)%2==0:
                d+="0"
            else:
                d+="1"
        if d == "10101" or d == "01010":
            cnt+=1


print(cnt)