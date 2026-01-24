
def f(a):
    return 2*a

def g(a):
    return 3*a

P,Q =map( f, range(1, 11)), map( g, range(1, 11))

def X(A,x):
    return ((x in A) <= (x in P)) and not (x in A)


for A in range(100):
    if all(X(A,x) for x in range(100)):
        print(A)