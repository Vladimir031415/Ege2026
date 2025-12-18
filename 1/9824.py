from itertools import permutations
m = "346 45 16 125 247 137 56".split()
g = "GD GE DE DF EC FA AC AB CB".split()
for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x,y in g):
        print(*i)