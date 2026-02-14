from functools import lru_cache

def F(n):
    return G(n-1)

@lru_cache(None)
def G(n):
    if n < 10: return 3*n
    return G(n-2) + 2

for i in range(4, 47990):
    G(i)

print(F(47995))