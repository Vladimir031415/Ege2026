def f(x, s):
    if x <= 11: return s%2 == 0
    if s <= 0: return False
    h = [f(x-3, s-1), f(x-7, s-1), f(x//3, s-1)]
    if (s-1)%2 == 0: return any(h)
    else: return all(h)

print([x for x in range(12, 50) if f(x,2)])
print([x for x in range(12, 50) if f(x,3) and not f(x,1)])
print([x for x in range(12, 50) if f(x,4) and not f(x,2)])