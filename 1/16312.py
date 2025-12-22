from itertools import permutations
m = "37 57 147 37 26 57 12346".split()
g = "AD AC AG CD GD DE DB EF BF".split()

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x, y in g):
        print(*i)