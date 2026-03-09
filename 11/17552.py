from math import *
for i in range(1,50):
    if ceil(261 * i / 8) * 252500 > 31 * 2 ** 20:
        print(i)
        break