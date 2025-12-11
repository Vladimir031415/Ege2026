from string import printable

for i in printable[:19]:
    a1 = int(f"78{i}79643",19)
    a2 = int(f"25{i}43", 19)
    a3 = int(f"63{i}5", 19)
    a = a1 + a2 + a3
    if a % 18 == 0:
        print(a/18)
