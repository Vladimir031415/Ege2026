from itertools import permutations
m = "457 567 45 136 123 247 126".split()
g = "AB AD AF FD DC CB FE EC EG GB".split()
for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x,y in g):
        print(*i)