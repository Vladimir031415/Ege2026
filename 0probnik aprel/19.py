def f(x, s):
    if s < 0: return False
    if x < 16: return s % 2 == 0
    if (s - 1) % 2 == 0: return any([f(x-3, s-1), f(x-8, s-1), f(x//3, s-1)])
    return all([f(x - 3, s - 1), f(x - 8, s - 1), f(x // 3, s - 1)])

print([i for i in range(17, 300) if f(i, 2)])
print([i for i in range(17, 300) if f(i, 3) and not f(i, 1)])
print([i for i in range(17, 300) if f(i, 4) and not f(i, 2)])