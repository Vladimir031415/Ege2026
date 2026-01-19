a = []
def g(A,x):
    return (x&A==0) <= ((x&77 == 0) and(x&44 == 0))
for A in range(1,200):
    if all(g(A,x) for x in range(1,200)):
        print(A)
        break