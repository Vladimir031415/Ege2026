def f(start, end, cnt):
    if start == end and cnt > 50: return 1
    if start > end: return 0
    return f(start + 2, end, cnt + 1) + f(start * 3, end, cnt + 1) + f(start * 4, end, cnt + 1)
print(f(2, 400, -1))