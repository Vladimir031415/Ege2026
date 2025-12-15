from itertools import permutations
cnt = 0
for val in set(permutations("PARIGANKA")):
    val = "".join(val)
    if "AA" in val and "AAA" not in val:
        cnt+=1
print(cnt)