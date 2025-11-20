from string import printable
a = []
for y in printable[9:14]:
    for x in printable[int(y, 15)+1:14]:
        n1 = int(f"7{x}37{y}", 23)
        n2 = int(f"9{y}63", int(x,16))
        n3 = int(f"15148", int(y,16))
        print(n1+n2+n3 , (n1+n2+n3)//(int(x,16)+int(y,16)))