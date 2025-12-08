from itertools import *

alph = "ДИОНСЙ"
d = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = "".join(val)
    if val.count("Д") >= 0 or val.count("Н") >= 0:
        if not(val.count("Д") >= 0 and val.count("Н") >= 0):
            e = 0
            for i in range(5):
                if val[i] != val[i]:
                    e+=1
            if e == 5:
                d+=1
print(d)