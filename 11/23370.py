from math import *
for L in range(1, 10**8):
    i = 5
    I = ceil(L*i/8)
    if 7_564_230 * I > 31 * 2**20:
        print(L)
        break