from itertools import *

alph = sorted("АЛГОРИТМ")
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = "".join(val)
    if val[0] not in "АГ" and val.count(R)>=2:
        print(pos,val)
