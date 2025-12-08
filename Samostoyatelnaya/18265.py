for p in range(30,37):
    for s in range(10, 35):
        n1 = int("R4", p-1)
        n2 = int("B0", s+2)
        n3 = int("T3NK4", p)
        n = n1+n2+n3
        if n == 23593399:
            print(p*s)
