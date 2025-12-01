from itertools import *


#permutations
alph = "122"
for i in permutations(alph):
    i = "".join(i)
    print(i)


print("")


for i in permutations(alph,2):
    i = "".join(i)
    print(i)

#product

#enumirate - нумерует начиная от start=n

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = "".join(val)
    if val[0] not in "АБВ":
        print(pos)