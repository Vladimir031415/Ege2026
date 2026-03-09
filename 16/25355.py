from sys import setrecursionlimit

setrecursionlimit(300000)

def G(n):
    if n >= 248045: return int(n/20 + 28)
    else: return G(n + 9) - 4

def F(n):
    if n < 19: return 6*(G(n-7)-36)
    return F(n-4) + 3580

print(F(673))