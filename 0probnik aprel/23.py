def a(s,f):
    if s == f: return 1
    if s <= f: return 0
    if s == 7: return 0
    return sum([a(s-1, f), a(s-4, f), a(s//3, f)])
print(a(19,2), a(19,13),a(13,2),a(19,13)*a(13,2))