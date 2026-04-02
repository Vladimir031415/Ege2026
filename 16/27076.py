from sys import setrecursionlimit
setrecursionlimit(10000)
def f(n):
    if n < 43: return g(n+4)
    return 2*f(n-2) - f(n-4) + 2
def g(n):
    if n < 11240: return g(n+3) + 2
    return q(n)
def q(n):
    if n < 21: return n+4
    return q(n-4) + 2
print(f(2026))
