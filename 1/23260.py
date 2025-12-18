from itertools import permutations
matrix = "346 348 12 127 578 15 458 257".split()
graph = "AD DC CF FG GE EA HA HG HB BC BD".split()

for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

