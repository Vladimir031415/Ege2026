from itertools import permutations
cnt = 0
for val in set(permutations("KIDALA" , 5)):
    val = "".join(val)
    if "AA" not in val:
        cnt+=1
print(cnt)
