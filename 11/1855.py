from math import *
def roof(a):
    return ceil(a)
L = 101
N = 4090 + 10
i = roof(log2(N))
I = roof(L * i/8)
print(2048 * I / 1024)
