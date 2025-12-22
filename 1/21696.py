from itertools import permutations
m = "23 168 158 578 347 27 456 234".split()
g = "AE AF ED DF EH DB FC CG HB GB HG".split()
for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in m[i.index(y)] for x,y in g):
        print(*i)
