t = "0123456789abcdefghijklmnopqrstuvwxyz"
r = 0
for i in t[:29]:
    if (int(f"923{i}874", 29) + int(f"524{i}6152", 29))%28 == 0:
        print(r)
    r += 1
