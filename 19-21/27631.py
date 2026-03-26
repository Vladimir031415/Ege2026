def f(x,y, s):
    if x + y >= 211: return s%2 == 0
    if s <= 0: return False
    h = [f(x+1, y, s-1), f(x*2, y, s-1), f(x, y*2, s-1), f(x, y+1, s-1)]
    if (s-1) % 2 == 0: return any(h)
    else: return all(h)

print([x for x in range(1, 194) if f(x, 17, 2)])
print([x for x in range(1, 194) if f(x, 17, 3) and not f(x, 17, 1)])
print([x for x in range(1, 194) if f(x, 17, 4) and not f(x, 17, 2)])