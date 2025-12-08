from itertools import *

alph = "ПОЛИНА"
d = 0
for pos, val in enumerate(product(alph, repeat=8), start=1):
    val = "".join(val)
    if val.count("П")+val.count("Л")+val.count("Н") >= val.count("О")+val.count("И")+val.count("А"):
        d+=1
print(d)

