from itertools import permutations
cnt = 0
for val in set(permutations("РОСОМАХА")):
    val = "".join(val)
    val.replace("Р","1").replace("С","1").replace("М","1").replace("Х","1").replace("А","0").replace("О","0")
    if "11" not in val and "22" not in val:
        cnt+=1
print(cnt)