from sys import setrecursionlimit

setrecursionlimit(300000)

def G(n):
    if n >= 28: return G(n - 5) - 15
    return 3*n - 4

def F(n):
    if n >= 31054: return 3*(G(n-2)-15)
    return F(n+4) + 3020

print(F(15))