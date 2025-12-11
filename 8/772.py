from itertools import permutations
cnt = 0
for val in set(permutations("ПРОБНИК")):
    val = "".join(val)
    if val[0] in "ПРБНК" and val[6] in "ПРБНК" and "ОИ" not in val and "ИО" not in val and "ОО" not in val and "ИИ" not in val:
        cnt += 1
print(cnt)