from itertools import permutations
cnt = 0
for i in permutations("KAYF"):
    i = "".join(i)
    if i[3] != "Y" and "KF" not in i:
        cnt += 1
print(cnt)
