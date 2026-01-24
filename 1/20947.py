from itertools import permutations
m = "267 157 468 356 248 134 12 35".split()
g = "AB AV VB BG VD GJ DJ GI JI IE ED".split()
for i in permutations("ABVGDEJI"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g):
        print(*i)