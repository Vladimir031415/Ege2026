from string import printable

for i in printable[:19]:
    n1 = int(f"98{i}79641", 19)
    n2 = int(f"36{i}14", 19)
    n3 = int(f"73{i}4", 19)
    if (n1+n2+n3)%18 == 0:
        print((n1+n2+n3)//18)
        break
