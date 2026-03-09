def f(x,y, s):
    if x + y <= 100: return s%2 == 0
    if s <= 0: return False
    h = [f(x-3, y-3, s-1), f(x//2, y, s-1), f(x, y//2, s-1)]
    if (s-1) % 2 == 0: return any(h)
    else: return all(h)

print([x for x in range(53, 200) if f(x, 48, 2)])
print([x for x in range(53, 200) if f(x, 48, 3) and not f(x, 48, 1)])
print([x for x in range(53, 200) if f(x, 48, 4) and not f(x, 48, 2)])