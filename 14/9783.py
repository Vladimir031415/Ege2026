from string import printable

for i in printable[:22]:
    n1 = int(f"18{i}89957", 22)
    n2 = int(f"80{i}33", 22)
    n3 = int(f"521{i}6", 22)
    if (n1+n2+n3)%21 == 0:
        print((n1+n2+n3)//21)
        break