from itertools import permutations
m = "247 148 578 126 38 47 136 235".split()
g = "BA AH HB AE HF FG EG FD EC CD GC".split()
for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x,y in g):
        print(*i)