t = "0123456789abcdefghijklmnopqrstuvwxyz"

for i in t[:25]:
    a = int(f"A4{i}7F2", 25)
    b = int(f"N{i}G5{i}H", 25)
    c = int(f"74{i}M26", 25)
    if (a+b+c)%24 == 0:
        print((a+b+c)/24)