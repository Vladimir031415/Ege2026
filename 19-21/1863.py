def f(x, s):
    if x >= 40: return s % 2 == 0
    if s == 0: return False
    h = [f(x+1, s-1), f(x+4, s-1), f(x*2, s-1)]
    if (s-1)%2 == 0: return any(h)
    else:return all(h)

print("19)", [x for x in range(1, 40) if f(x,2)])
print("20)", [x for x in range(1, 40) if f(x,3) and not f(x, 1)])
print("21)", [x for x in range(1, 40) if f(x,4) and not f(x, 2)])
    