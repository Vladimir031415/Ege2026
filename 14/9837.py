from string import printable

for i in printable[:23]:
    n1 = int(f"7{i}38596", 23)
    n2 = int(f"14{i}36", 23)
    n3 = int(f"61{i}7", 23)
    if (n1+n2+n3)%22 == 0:
        print((n1+n2+n3)//22)
        break