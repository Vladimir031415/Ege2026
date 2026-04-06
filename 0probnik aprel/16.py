from sys import setrecursionlimit
setrecursionlimit(6000)
def f(a): return 3 * (g(a-2) + 5)
def g(n):
    if n < 8: return n * 3
    return g(n-3) + 2
print(f(12345))
