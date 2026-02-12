def g(A,x,y):
    return (78125 != y + 4*x) or ((A>x) and (A>y))
for A in range(1,100000):
    if all(g(A, x, y) for x in range(1,200) for y in range(1,200)):
        print(A)
        break