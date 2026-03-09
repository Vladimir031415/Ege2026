def f(x,y, s):
    if x + y >= 77: return s%2 == 0
    if s <= 0: return False
    h = [f(x+3, y, s-1), f(x*3, y, s-1), f(x, y+3, s-1), f(x, y*2, s-1)]
    if (s-1) % 2 == 0: return any(h)
    else: return all(h)

print([x for x in range(1, 64) if f(x, 12, 2)])
print([x for x in range(1, 64) if f(x, 12, 3) and not f(x, 12, 1)])
print([x for x in range(1, 64) if f(x, 12, 4) and not f(x, 12, 2)])