def f(A,x,y):
    return ((A < x) or (x**2 - 7*x + 10 > 0)) and ((A>=y or (y**2 + 7*y +12 > 0)))
cnt = 0
for A in range(-100, 100):
    if all([f(A,x,y) for x in range(-50, 50) for y in range(-50, 50)]):
        cnt += 1
print(cnt)