def g(A,x):
    return (A + 2 * x > 400 - A) and (A%100 + 120%A > 140)
for A in range(0,1000):
    if all(g(A,x) for x in range(1,200)):
        print(A)
        break